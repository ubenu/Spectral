# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:29:53 2017

@author: schilsm
"""

import copy
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from scipy.optimize import curve_fit

pd.options.mode.chained_assignment = None  
# suppresses unnecessary warning when creating self.working_data

class SpectralCurve():
    # Class attributes - same for all objects
    columns = ['X', 'Y1', 'Y2',]
    techniques = ['CD', 'Fluorescence', 'Absorbance']
    x_units = ['nm', 'celcius', 'seconds', ]
    y2_units = ['V', ]
    technique_y_units = {'CD': ['mdeg', 'dAbs', 'dEps_mrw', 'dEps_M',],
                          'Fluorescence': ['intensity'],
                          'Absorbance': ['absorbance']
                          }
    stats = ['min', 'max','avg', 'std', ]
    # End class attributes
    
    def __init__(self, key, data, technique, units_x, units_y, **kwargs):
        self.key = key
        self._original_data = data.sort_values(by='X', ascending=True) 
        self._original_data.index = self._original_data['X']
        self.working_data = copy.deepcopy(self._original_data)
        self.attributes = {'technique': None,
                          'x_units': None,
                          'y_units': None,
                          'y2_units': None,
                          'factor': 1.0,
                          'offset': 0.0,
                          'n_deriv': 0,
                          'conc_M': 1.0e-5,
                          'conc_gpl': 1.0,
                          'mrw': 111.0,
                          'path_length': 0.1,
                          'composition': None,
                          }
        self.attributes['technique'] = technique
        self.attributes['x_units'] = units_x
        self.attributes['y_units'] = units_y
        for kw in kwargs:
            self.attributes[kw] = kwargs[kw]
        self._original_attributes = copy.deepcopy(self.attributes)
        if self.mdeg_units(): # It's a CD spectrum
            self.align_cd_to_zero()
            self.convert('dAbs')
            
            
    def get_scatter_params(self, x_lo, x_hi, constants, params0):
        d = copy.deepcopy(self.working_data[['X','Y1']])
        dl = d[d['X'] >= x_lo]
        d = dl[dl['X'] <= x_hi]
        try:
            params, covar = curve_fit(self.make_calc_scatter(constants), 
                                      d['X'], d['Y1'], p0=params0)
        except Exception as e:
            print(e)
            
        return params
    
    def make_calc_scatter(self, constants):
        p = constants['power']
        def calc_scatter(x, *variables):
            a0, c = variables
            return a0 + np.power(c / x, p)
        return calc_scatter
            
    def mdeg_units(self):
        return (self.attributes['technique'] == 'CD' and 
                self.attributes['y_units'] == 'mdeg')
                   
    def x_min(self):
        return self.get_column_stats('X', 'min')
        
    def x_max(self):
        return self.get_column_stats('X', 'max')
                
    def x_step(self):
        """
        Returns avg step size for a step whose std/avg is smaller than rtol
        (??? rtol doesn't appear to have been used)
        or 0.0 otherwise (this is an irregular step)
        """
        avg_step = self.get_interval_stats('X', 'avg')
        std_step = self.get_interval_stats('X', 'std')
        return (avg_step, std_step)
    
    def y_min(self):
        return self.get_column_stats('Y1', 'min')
        
    def y_max(self):
        return self.get_column_stats('Y1', 'max')
        
    def y_avg(self):
        return self.get_column_stats('Y1', 'avg')
        
    def y_std(self):
        return self.get_column_stats('Y1', 'std')  
    
    def is_equal(self, attr_name, value):
        if attr_name == 'x_min':
            return value == self.x_min()
        elif attr_name == 'x_max':
            return value == self.x_max()
        else:
            return self.attributes[attr_name] == value
            
    def get_column_stats(self, column_id, stats_id):
        d = self.working_data[column_id]
        if stats_id == 'min':
            return d.min()
        if stats_id == 'max':
            return d.max()
        if stats_id == 'avg':
            return d.mean()
        if stats_id == 'std':
            return d.std()

    def get_interval_stats(self, column_id, stats_id):
        d1 = self.working_data[column_id].iloc[0:-2].as_matrix()
        d2 = self.working_data[column_id].iloc[1:-1].as_matrix()
        diff = d2 - d1
        if stats_id == 'min':
            return diff.min()
        if stats_id == 'max':
            return diff.max()
        if stats_id == 'avg':
            return diff.mean()
        if stats_id == 'std':
            return diff.std()
        
    def align_cd_to_zero(self, align_range=10):
        align_min = self.x_max() - align_range
        if align_min < self.x_min():
            align_range = self.x_max() - self.x_min()
        n_datapoints = int(align_range / self.x_step()[0]) + 1
        mean_align = self.working_data.iloc[-n_datapoints:].mean()['Y1']
        self.working_data['Y1'] -= mean_align
        
    def convert(self, target_units):
        # First, convert CD data to a standard unit (mdeg)
        self.convert_to_mdeg()
        # Then convert them to the target
        f = 1.0/32980.0
        p = self.attributes['path_length']
        c = self.attributes['conc_gpl']
        m = self.attributes['conc_M']
        r = self.attributes['mrw']

        if target_units == 'mdeg':
            f = 1.0
        if target_units == 'dAbs':
            f *= 1.0
        if target_units == 'dEps_mrw':
            f *= r / (p * c)
        if target_units == 'dEps_M':
            f *= 1 /(p * m)
        self.working_data['Y1'] *= f
        self.attributes['y_units'] = target_units
        
    def convert_to_mdeg(self):     
        f = 32980.0
        p = self.attributes['path_length']
        c = self.attributes['conc_gpl']
        m = self.attributes['conc_M']
        r = self.attributes['mrw']
        if self.attributes['y_units'] == 'mdeg':
            f = 1.0        
        if self.attributes['y_units'] == 'dAbs':
            f *= 1.0
        if self.attributes['y_units'] == 'dEps_mrw':
            f *=  (p * c / r) 
        if self.attributes['y_units'] == 'dEps_M':
            f *= (p * m)
        self.working_data['Y1'] *= f
        self.attributes['y_units'] = 'mdeg'
    
    def resample(self, startx=0.0, stopx=0.0, dx=0.0):
        data = copy.deepcopy(self.working_data)
        old_x = data['X'].as_matrix()
        if startx == stopx:
            startx, stopx = np.floor(old_x.min()), np.ceil(old_x.max())
        if dx == 0.0:
            dx = self.x_step()[0]
        x_arr = np.arange(startx, stopx+dx, dx, dtype=float)
        np.around(x_arr, decimals=3, out=x_arr)
        mask = np.logical_and((x_arr >= old_x.min()), 
                              (x_arr <= old_x.max()))
        new_x = x_arr[mask]
        xx = np.vstack((new_x, np.ones_like(new_x))).transpose()
        dfxx = pd.DataFrame(xx, columns=['X', 'Keep'])
        # merged = pd.ordered_merge(data, dfxx, on='X') 
        # ordered_merge has been deprecated
        merged = pd.merge_ordered(data, dfxx, on='X')
        merged.index = merged['X']
        mask = (merged['Keep'] == 1.0).as_matrix()
        intp_merged = merged.interpolate(method='values')[data.columns]
        self.working_data = intp_merged[mask]
        
    def apply_factor(self, factor):
        old_factor = self.attributes['factor']
        self.working_data['Y1'] *= (factor / old_factor)
        self.attributes['factor'] = factor
        self.attributes['offset'] *= (factor / old_factor)
        
    def apply_offset(self, offset):
        old_offset = self.attributes['offset']
        self.working_data['Y1'] += (old_offset - offset)
        self.attributes['offset'] = offset
        
    def restrict_x(self, x_min, x_max):
        x = self.working_data['X']
        mask = np.logical_and(x >= x_min, x <= x_max)
        self.working_data = self.working_data[mask]
        
    def subtract_curve(self, other):
        self.working_data['Y1'] -= other.working_data['Y1']
        
    def reset_to_original(self):
        self.working_data = copy.deepcopy(self._original_data)
        self.attributes = copy.deepcopy(self._original_attributes)
        if self.mdeg_units():
            self.convert('dAbs')

    def smooth_deriv(self, window, poly_ord, deriv):
        d, dd = self.x_step()
        step =  abs(d) 
        if step > 0.0:  # cannot smooth an irregularly samples curve
            npoints = int(window / step)
            npoints = npoints - npoints % 2 + 1 # must be an odd integer
            if poly_ord >= npoints:
                poly_ord = npoints - 1  # poly_ord must be smaller than npoints
            if poly_ord == 0 and npoints == 1:
                poly_ord = 1
                npoints = 3
            x = self.working_data['Y1'].as_matrix()
            try:
                y = savgol_filter(x, npoints, poly_ord, deriv)
            except ValueError as e:
                print(e.strerror)
            except:
                print("Other error in savgol_filter")
                
            self.working_data['Y1'] = y
            if deriv > 0:
                self.attributes['n_deriv'] = self.attributes['n_deriv'] + 1
                        
    def create_cdpro_input(self):
        content = ""
        d, dd = self.x_step() 
        pro_factor = 1.0
        x = self.working_data['X'].as_matrix()
        mask = [x % 1.0 < 0.999 * d] 
        # factor 0.999 introduced to avoid the occasional .2 appearing
        out_x = x[mask]
        wl_min, wl_max = out_x.min(), out_x.max()
        data = self.working_data['Y1'].as_matrix()
        out_data = data[mask]
        content +=  "#\n#\n0 7\n#\n#\n"
        content += self.key
        content += "\n#\n#\n"
        content += '{} {} {}'.format(wl_max, wl_min, pro_factor)
        content += "\n#\n#\n"
        for i in out_data:
            content += ' {:.3e}'.format(i)
        content += "\n#\n#\n 0 \n"
        return content