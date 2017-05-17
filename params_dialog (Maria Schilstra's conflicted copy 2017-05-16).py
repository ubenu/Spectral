# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:22:35 2017

@author: schilsm
"""
import pandas as pd, numpy as np

from PyQt5 import QtCore as qt
from PyQt5 import QtWidgets as widgets

import params_dialog_ui as ui

#from PyQt5.uic import loadUiType
#Ui_ParamsDialog, QDialog = loadUiType('params_dialog.ui')

class ParamsDialog(widgets.QDialog, ui.Ui_ParamsDialog):

    col_nrs = range(6)
    (id_path, id_mrw, id_conc_gpl, id_conc_M, id_mw, id_n) = col_nrs
    headers = ('Path length \n(cuvette)', 
               'Mean residue \nweight (g/mol)', 
               'Concentration\nin mg/ml', 
               'Concentration\nin mol/L', 
               'Mol. weight\n(g/mol)', 
               'Nr of\nresidues',
               )


    def __init__(self, parent, data, target):
        super(widgets.QDialog, self).__init__(parent)
        self.setupUi(self)
        self.tbl_params.itemChanged.connect(self.on_item_changed)
        self.tbl_params.currentItemChanged.connect(self.on_current_item_changed)
        #self.tbl_params.setStyleSheet("QTableView {selection-background-color: red;}")
        
        self.data = data
        
        keys = data.index
        self.data1 = pd.DataFrame(np.zeros((len(keys), len(self.col_nrs)),dtype=float))
        self.data1.index = keys
        self.data1.columns = self.headers
        p = self.data['path_length']
        c = self.data['conc_gpl']
        m = self.data['conc_M']
        r = self.data['mrw']
        w = c/m
        n = w/r
        self.data1.iloc[:, self.id_path] = p
        self.data1.iloc[:, self.id_conc_gpl] = c
        self.data1.iloc[:, self.id_conc_M] = m
        self.data1.iloc[:, self.id_mrw] = r
        self.data1.iloc[:, self.id_mw] = w
        self.data1.iloc[:, self.id_n] = n

        self.target = target
        self.create_table()
        self.set_all()
        
    def create_table(self):
        hh = [h for h in self.headers]
        vh = self.data1.index.values.tolist()
            
        self.tbl_params.setColumnCount(len(self.data1.columns))
        self.tbl_params.setRowCount(len(self.data1.index.values))
        self.tbl_params.setHorizontalHeaderLabels(hh)
        self.tbl_params.setVerticalHeaderLabels(vh)
        self.tbl_params.verticalHeader().setDefaultAlignment(qt.Qt.AlignRight)

        for row in range(self.tbl_params.rowCount()):
            for col in range(self.tbl_params.columnCount()):
                ti = widgets.QTableWidgetItem()
                ti.setText('{:.3g}'.format(self.data1.iloc[row, col]))
                self.tbl_params.setItem(row, col, ti)

                # Toggle (?? apparently - here: disable) enabled-ness of ti
                if self.target == 'dAbs':
                    if col in (self.id_path, self.id_mrw, self.id_conc_gpl, 
                               self.id_conc_M, self.id_mw, self.id_n):
                        ti.setFlags(qt.Qt.ItemIsEnabled)
                if self.target == 'dEps_mrw':
                    if col not in (self.id_path, self.id_mrw, self.id_conc_gpl):
                        ti.setFlags(qt.Qt.ItemIsEnabled)
                if self.target == 'dEps_M':
                    if col not in (self.id_path, self.id_conc_M, self.id_mw, 
                               self.id_n):
                        ti.setFlags(qt.Qt.ItemIsEnabled)            
        self.tbl_params.resizeColumnsToContents()
        self.tbl_params.resize(self.tbl_params.sizeHint())        
        
    def set_all(self):
        for row in range(self.tbl_params.rowCount()):
            for col in range(self.tbl_params.columnCount()):
                ti = self.tbl_params.item(row, col) # widgets.QTableWidgetItem()
                if not ti is None:
                    ti.setText('{:.3g}'.format(self.data1.iloc[row, col]))
        self.data['path_length'] = self.data1.iloc[:, self.id_path]
        self.data['conc_gpl'] = self.data1.iloc[:, self.id_conc_gpl]
        self.data['conc_M'] = self.data1.iloc[:, self.id_conc_M]
        self.data['mrw'] = self.data1.iloc[:, self.id_mrw]
        
    def on_item_changed(self, item):
        class NotANumberError(Exception): pass        
        class ZeroError(Exception): pass        
        try:
            if not self.is_number(item.text()):
                raise NotANumberError("Entry must be a number") 
            if not float(item.text()) > 0.0:
                raise ZeroError("Entry must be greater than zero") 
        except NotANumberError as e:
            widgets.QMessageBox.warning(self, "Error", str(e))
            item.setFocus()
            return    
        except ZeroError as e:
            widgets.QMessageBox.warning(self, "Error", str(e))
            item.setFocus()
            return    
            
        col, row = item.column(), item.row()
        if float(item.text()) != self.data1.iloc[row,col]:
            self.data1.iloc[row,col] = float(item.text())
            m = self.data1.iloc[row, self.id_conc_M]
            c = self.data1.iloc[row, self.id_conc_gpl]
            r = self.data1.iloc[row, self.id_mrw]
            w = self.data1.iloc[row, self.id_mw]
            n = self.data1.iloc[row, self.id_n]
            if col == self.id_conc_gpl:
                self.data1.iloc[row, self.id_conc_M] = c / w
            elif col == self.id_mrw:
                self.data1.iloc[row, self.id_n] = w / r
            elif col == self.id_conc_M:
                self.data1.iloc[row, self.id_conc_gpl] = w * m
            elif col == self.id_mw:
                self.data1.iloc[row, self.id_conc_gpl] = w * m
            elif col == self.id_n:
                self.data1.iloc[row, self.id_mrw] = w / n
            self.set_all()
            
            
    def on_current_item_changed(self, curr_item, prev_item):
        if not prev_item is None:
            col, row = prev_item.column(), prev_item.row()
            prev_item.setText('{:.3g}'.format(self.data1.iloc[row, col]))
        
    def get_params(self):
        return self.data
            
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False        
                      
        

        
            
        
