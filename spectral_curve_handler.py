# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:32:07 2017

@author: schilsm
"""

import copy
import numpy as np
import pandas as pd
from spectral_curve import SpectralCurve

pd.options.mode.chained_assignment = None  
# suppresses unnecessary warning when creating self.working_data

class SpectralCurveHandler():
    unit_ids = {'NANOMETERS': 'nm',
                'CD [mdeg]': 'mdeg',
                'HT [V]': 'V',
                'ABSORBANCE': 'absorbance',
                'Temperature[C]': 'celcius',
                'INTENSITY': 'intensity', 
                'F': 'intensity',
                'SEC': 'seconds',
                }
    operations = ['sum', 
                  'product', 
                  'mean', 
                  'std',
                  ]
    curves = None
    curve_nr = 0
    
    def __init__(self):
        self.curves = {}
        
    def read_input_file(self, key, file):
        file_content = pd.read_table(file, names=['Col1', 'Col2', 'Col3'])
        technique = self.get_technique(file_content)
        x_units, y_units, y2_units = self.get_axes_units(file_content)
        data = self.get_curve(file_content)
        curve = SpectralCurve(key, 
                              data, 
                              technique, 
                              x_units, 
                              y_units, 
                              y2_units=y2_units,
                              )
        return curve
    
    def suitable_for_cdpro(self, keys):
        suitable = False
        if len(keys) > 0:
            suitable = True
            for key in keys:
                curve = self.curves[key]
                suitable = suitable and curve.attributes['technique'] == 'CD'
                suitable = suitable and curve.attributes['x_units'] == 'nm'
                suitable = suitable and curve.attributes['y_units'] == 'dEps_mrw'
        return suitable
    
    def suitable_for_conversion(self, keys):
        suitable = False
        if len(keys) > 0:
            suitable = True
            for key in keys:
                curve = self.curves[key]
                suitable = suitable and curve.attributes['technique'] == 'CD'
        return suitable
    
    def suitable_for_scatter_correction(self, keys):
        suitable = False
        if len(keys) > 0:
            suitable = True
            for key in keys:
                curve = self.curves[key]
                suitable = suitable and curve.attributes['technique'] == 'Absorbance'
                suitable = suitable and curve.attributes['x_units'] == 'nm'
        return suitable        
    
    def suitable_for_bl_subtraction(self, keys):
        suitable = False
        if len(keys) > 0:
            suitable = True
            for key in keys:
                curve = self.curves[key]
                suitable = suitable and curve.attributes['x_units'] == 'nm'
        return suitable   

    def curves_overlap(self, keys):
        overlap = False
        if len(keys) > 0:
            x_stats = self.get_stats(keys, column_id='X')
            min_x = x_stats['Minimum X'].max()
            max_x = x_stats['Maximum X'].min()
            if min_x < max_x:
                overlap = True
        return overlap
    
    def suitable_for_combination(self, keys):
        suitable = False
        if len(keys) > 0:
            x_stats = self.get_stats(keys, column_id='X')
            min_x = x_stats['Minimum X'].max()
            max_x = x_stats['Maximum X'].min()
            if min_x < max_x:  # the curves overlap
                std = np.asarray(x_stats['Std step'])
                if round(std.sum(), 5) == 0.0:  # none of the curves has irregular x-data
                    steps = np.asarray(x_stats['Step X'])
                    if round(steps.std(), 5) == 0.0: # all curves have the same step size
                        suitable = True
                        for key in keys: 
                            data = self.curves[key].working_data['X']
                            suitable = suitable and (min_x in data or 
                                                     max_x in data)
        return suitable
        
    def add_curve(self, curve):
        key = curve.key
        self.curves[key] = curve
        self.curve_nr += 1
        
    def remove_curves(self, keys):
        for key in keys:
            self.curves.pop(key)
            
    def copy_curves(self, keys, new_keys):
        for key, new_key in zip(keys, new_keys):
            copied_curve = copy.deepcopy(self.curves[key])
            copied_curve.key = new_key
            self.add_curve(copied_curve)
                    
    def create_output(self, keys):
        frames = []
        for key in keys:
            curve = self.curves[key]
            frame = curve.working_data[['X','Y1']]
            frame.columns = ['X', key]
            frames.append(frame)
        result = pd.concat(frames, axis=1)
        return result.to_csv(index=False)
    
    def create_cdpro_input(self, keys):
        output = []
        for key in keys:
            curve = self.curves[key]
            output.append([curve.create_cdpro_input()])
        return output
    
    def reset_to_original(self, keys):
        for key in keys:
            curve = self.curves[key]
            curve.reset_to_original()
    
    def resample(self, keys, startx, stopx, dx):
        for key in keys:
            self.curves[key].resample(startx, stopx, dx)
            
    def smooth_curves(self, keys, wind_len, poly_ord, deriv):
        for key in keys:
            curve = self.curves[key]
            curve.smooth_deriv(wind_len, poly_ord, deriv)
            
    def get_stats(self, keys, column_id='Y1'):
        stats = pd.DataFrame(np.zeros((len(keys), 4),dtype=float))
        stats.index = keys
        if column_id == 'Y1':
            stats.columns = ['Minimum Y', 'Maximum Y', 'Average Y', 'StDev Y']
            for key in keys:
                curve = self.curves[key]
                n, x, a, s = curve.y_min(), curve.y_max(), curve.y_avg(), curve.y_std()
                stats.loc[key] = np.array([n, x, a, s])
        elif column_id == 'X':
            stats.columns = ['Minimum X', 'Maximum X', 'Step X', 'Std step']
            for key in keys:
                curve = self.curves[key]
                n, x = curve.x_min(), curve.x_max()
                (a, s) = curve.x_step()
                stats.loc[key] = np.array([n, x, a, s])
        return stats
    
    def get_conversion_params(self, keys):
        params = pd.DataFrame(np.zeros((len(keys), 4),dtype=float))
        params.columns = ['path_length', 'mrw', 
                          'conc_gpl', 'conc_M',
                          ]
        params.index = keys
        for key in keys:
            curve = self.curves[key]
            p = curve.attributes['path_length']
            c = curve.attributes['conc_gpl']
            m = curve.attributes['conc_M']
            r = curve.attributes['mrw']

            params.loc[key] = np.array([p, r, c, m])
        return params
    
    def set_conversion_params(self, params):
        for key in params.index:
            curve = self.curves[key]
            curve.attributes['path_length'] = params.loc[key]['path_length']
            curve.attributes['conc_gpl'] = params.loc[key]['conc_gpl']
            curve.attributes['conc_M'] = params.loc[key]['conc_M']
            curve.attributes['mrw'] = params.loc[key]['mrw']
    
    def convert(self, keys, target_units): # untested - check!
        for key in keys:
            curve = self.curves[key]
            curve.convert(target_units)

    def subtract_baseline(self, keys, bl_key, file):
        bl_key = bl_key + "=baseline"
        bl_curve = self.read_input_file(bl_key, file)
        self.add_curve(bl_curve)
        for key in keys:
            curve = self.curves[key]
            curve.subtract_curve(bl_curve)
        self.remove_curves([bl_key])
                
    def combine_curves(self, op, combi_key, keys, factors, inverted):
        technique, x_units, y_units, n_deriv = [], [], [], []      
        frames_x, frames_y = [], []
        for key, fac, inv in zip(keys, factors, inverted):
            curve = copy.deepcopy(self.curves[key])
            technique.append(curve.attributes['technique'])
            x_units.append(curve.attributes['x_units'])
            y_units.append(curve.attributes['y_units'])
            n_deriv.append(curve.attributes['n_deriv'])
            data_x = curve.working_data['X']
            data_y = curve.working_data['Y1'] * fac
            if inv:
                data_y = 1.0/data_y
            frames_x.append(data_x)
            frames_y.append(data_y)
        aggregate_x = pd.concat(frames_x, axis=1, join='inner', copy=False)
        df = pd.DataFrame(aggregate_x.mean(axis=1), columns=['X']) 
        aggregate_y = pd.concat(frames_y, axis=1, join='inner', copy=False)
        result = None
        if op == 'sum':
            result = aggregate_y.sum(axis=1)
        if op == 'product':
            result = aggregate_y.product(axis=1)
        if op == 'mean':
            result = aggregate_y.mean(axis=1)
        if op == 'std':
            result = aggregate_y.std(axis=1)
        if not result is None:
            df['Y1'] = result
            comp_str = op + "(" + keys[0]
            for k in keys[1:]:
                comp_str += (", " + k)
            comp_str += ")"
            curve = SpectralCurve(combi_key, 
                                  df, 
                                  np.unique(technique)[0], 
                                  np.unique(x_units)[0],
                                  np.unique(y_units)[0],
                                  composition=comp_str
                                  )
            return curve
        return None
            
    def attr_value_equal(self, key, attr_name, value):
        return self.curves[key].is_equal(attr_name, value)
    
    def modify(self, keys, attribute, values):
        for key, value in zip(keys, values):
            curve = self.curves[key]
            if attribute == 'factor':
                curve.apply_factor(value)
            elif attribute == 'offset':
                curve.apply_offset(value)
            elif attribute == 'x_min':
                x_max = curve.x_max()
                curve.restrict_x(value, x_max)
            elif attribute == 'x_max':
                x_min = curve.x_min()
                curve.restrict_x(x_min, value)
            else:
                pass
        
    def set_attributes(self, keys, **kwargs):
        for key in keys:
            curve = self.curves[key]
            for kw in kwargs:
                if kw in curve.attributes:
                    curve.attributes[kw] = kwargs[kw]
                    
    def get_curve(self, content):
        if self.file_origin(content) == 'Jasco':
            x_start = content.loc[content['Col1'] == 'FIRSTX']['Col2'].values[0].strip()
            x_end = content.loc[content['Col1'] == 'LASTX']['Col2'].values[0].strip()
            ind0 = content.loc[content['Col1'] == x_start].index[0]
            ind1 = content.loc[content['Col1'] == x_end].index[0]
            data = content.loc[ind0:ind1].astype(float)
            data.columns = ['X', 'Y1', 'Y2']
            data.index = data['X']
            return data
        return None
        
    def get_technique(self, content):
        technique = 'Unknown'
        if self.file_origin(content) == 'Jasco':
            y_units = \
            content.loc[content['Col1'] == 'YUNITS']['Col2'].values[0].strip()
            if y_units == 'CD [mdeg]':
                technique = 'CD'
            elif y_units in ['INTENSITY', 'F']:
                technique = 'Fluorescence'
            elif y_units == 'ABSORBANCE':
                technique = 'Absorbance'
        return technique
        
    def get_axes_units(self, content):
        if self.file_origin(content) == 'Jasco':
            x_units = \
            content.loc[content['Col1'] == 'XUNITS']['Col2'].values[0].strip()
            y_units = \
            content.loc[content['Col1'] == 'YUNITS']['Col2'].values[0].strip()
            y2_units = ''
            row = content.loc[content['Col1'] == 'Y2UNITS']
            if not row.empty:
                y2_units = row['Col2'].values[0].strip()
            if x_units in self.unit_ids:
                x_units = self.unit_ids[x_units] 
            if y_units in self.unit_ids:
                y_units = self.unit_ids[y_units] 
            if y2_units in self.unit_ids:
                y2_units = self.unit_ids[y2_units] 
            return x_units, y_units, y2_units
        return ''        

    def file_origin(self, content):
        if not content.loc[content['Col1'] == 'ORIGIN'].empty:
            if not content.loc[content['Col1'] == 'ORIGIN']['Col2'].empty:
                if content.loc[content['Col1'] == 'ORIGIN']['Col2'].values[0] == 'JASCO':
                    return 'Jasco'
        return ''      