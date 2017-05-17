# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:30:39 2017

@author: schilsm
"""
from PyQt5 import QtCore as qt
from PyQt5 import QtWidgets as widgets

import math_dialog_ui as ui

#from PyQt5.uic import loadUiType
#Ui_MathDialog, QDialog = loadUiType('math_dialog.ui')

class MathDialog(widgets.QDialog, ui.Ui_MathDialog):
    columns = range(4)
    (h_inc, h_id, h_fac, h_inv) = columns
    headers = {h_inc: "Curve",
               h_id: "File",
               h_fac: "Factor", 
               h_inv: "Invert",
               }
    operations = range(4)
    (o_sum, o_product, o_mean, o_stdev) = operations
    op_descr = {o_sum: "Sum",
                o_product: "Product",
                o_mean: "Average",
                o_stdev: "Stdev",
                }
    op_str = {o_sum: 'sum',
              o_product: 'product',
              o_mean: 'mean',
              o_stdev: 'std',
              }

    def __init__(self, parent):
        super(widgets.QDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.btn_ok.clicked.connect(self.close)
        self.btn_cancel.clicked.connect(self.on_cancel)

        self.btn_calc.clicked.connect(self.on_calc)
        #self.data_series = None
        labels = [self.headers[i] for i in self.columns]
        self.tbl_curves.setColumnCount(len(labels))
        self.tbl_curves.setHorizontalHeaderLabels(labels)
        self.tbl_curves.resizeColumnsToContents() 
        self.current_op = self.o_mean
        for i in self.op_descr:
            self.cmb_op.insertItem(i, self.op_descr[i])
        self.cmb_op.setCurrentIndex(self.current_op)
        self.txt_result_name.setText("combination")
        self.cmb_op.setSizeAdjustPolicy(widgets.QComboBox.AdjustToContents)
        self.new_keys = []
            
    def on_calc(self):
        op = self.op_str[self.cmb_op.currentIndex()]
        if self.txt_result_name.text() == "":
            self.txt_result_name.setText("combination")
        combi_key = self.txt_result_name.text()
        if combi_key not in self.new_keys:
            self.new_keys.append(combi_key)
        keys, facs, inv = [], [], []
        for row in range(self.tbl_curves.rowCount()):
            keys.append(self.tbl_curves.item(row, self.h_id).text())
            facs.append(float(self.tbl_curves.item(row, self.h_fac).text()))
            inv.append(self.tbl_curves.item(row, self.h_inv).checkState() == qt.Qt.Checked)
        self.parent().combine_curves(op, combi_key, keys, facs, inv)
        
    def on_cancel(self):
        keys = self.new_keys
        for key in keys:
            self.parent().ui_curves.pop(key)
        self.parent().curve_handler.remove_curves(keys)
        self.parent().remove_curves_from_table(keys)
        self.parent().plot_curves()
        self.close()

    def update_table(self, keys):
        for key in keys:
            row = self.find_table_item_row(key)
            if row == -1:
                row = self.tbl_curves.rowCount()
                self.tbl_curves.insertRow(row)
                for i in self.columns:
                    ti = widgets.QTableWidgetItem()
                    if i not in (self.h_inc, self.h_fac, self.h_inv):
                        ti.setFlags(qt.Qt.ItemIsEnabled)
                    if i in (self.h_inv, ):
                        ti.setCheckState(qt.Qt.Unchecked)
                    self.tbl_curves.setItem(row, i, ti)
                i_id = self.tbl_curves.item(row, self.h_id)
                i_id.setText(key)
            icon = self.parent().line_icon(self.parent().ui_curves[key]['color'] )
            ti = self.tbl_curves.item(row, self.h_inc)
            ti.setIcon(icon)
            ti = self.tbl_curves.item(row, self.h_fac)
            ti.setText('{:+.2f}'.format(1.0))
            ti = self.tbl_curves.item(row, self.h_inv)
        self.tbl_curves.resizeColumnsToContents()
        self.tbl_curves.resizeRowsToContents()
        
    def find_table_item_row(self, key):
        items = self.tbl_curves.findItems(key, qt.Qt.MatchExactly)
        if len(items) > 0:
            return self.tbl_curves.row(items[0])
        return -1 
        