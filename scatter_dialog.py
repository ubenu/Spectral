# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:55:28 2017

@author: SchilsM
"""

from PyQt5 import QtCore as qt
from PyQt5 import QtWidgets as widgets

from spectral_mpl import MplCanvas

import scatter_dialog_ui as ui

#from PyQt5.uic import loadUiType
#Ui_ScatterDialog, QDialog = loadUiType('scatter_dialog.ui')

class ScatterDialog(widgets.QDialog, ui.Ui_ScatterDialog):
    columns = range(7)
    (h_chk, h_id, h_x_max, h_x_min, h_exp, h_offs, h_amp) = columns
    headers = {h_chk: "View",
               h_id: "File",
               h_x_max: "High \nwavelength", 
               h_x_min: "Low \nwavelength",
               h_exp: "Exponent",
               h_offs: "Offset",
               h_amp: "Amplitude"
               }

    def __init__(self, parent, keys):
        super(widgets.QDialog, self).__init__(parent)
        self.setupUi(self)
        self.canvas = MplCanvas(self.mpl_window)
        self.mpl_layout.addWidget(self.canvas)
        labels = [self.headers[i] for i in self.columns]
        self.tbl_curves.setColumnCount(len(labels))
        self.tbl_curves.setHorizontalHeaderLabels(labels)
        self.tbl_curves.resizeColumnsToContents() 
        self.set_table_content(keys)
        self.chk_view_all.clicked.connect(self.on_view_all)
        self.tbl_curves.itemChanged.connect(self.on_item_changed)   
        self.chk_view_all.setCheckState(qt.Qt.Checked)
        self.on_view_all()
        self.plot_all()

    def on_view_all(self):
        chkd = qt.Qt.Unchecked
        if self.chk_view_all.isChecked():
            chkd = qt.Qt.Checked
        for row in range(self.tbl_curves.rowCount()):
            ti = self.tbl_curves.item(row, self.h_chk)
            ti.setCheckState(chkd)
            
    def on_item_changed(self, item):
        class NotANumberError(Exception): pass 
       
        col = item.column()
        if col in (self.h_x_min, self.h_x_max, self.h_exp):
            try:
                if not self.is_number(item.text()):
                    raise NotANumberError("Entry must be a number") 
            except NotANumberError as e:
                widgets.QMessageBox.warning(self, "Error", str(e))
                item.setFocus()
                return    
            row = item.row()
            key = self.tbl_curves.item(row, self.h_id).text()
            params = self.get_scatter_params(key)
            a0, pc = params
            ti_offs = self.tbl_curves.item(row, self.h_offs)
            ti_offs.setText(str(a0))
            ti_amp = self.tbl_curves.item(row, self.h_amp)
            ti_amp.setText(str(pc)) 
            self.tbl_curves.resizeColumnsToContents()
            self.tbl_curves.resizeRowsToContents()
        self.plot_all()

    def set_table_content(self, keys):
        for key in keys:
            curve = self.parent().curve_handler.curves[key]
            row = self.find_table_item_row(key)
            if row == -1:
                row = self.tbl_curves.rowCount()
                self.tbl_curves.insertRow(row)
                for i in self.columns:
                    ti = widgets.QTableWidgetItem()
                    if i in (self.h_id, self.h_offs, self.h_amp):
                        ti.setFlags(qt.Qt.ItemIsEnabled)
                    self.tbl_curves.setItem(row, i, ti)
                ti_id = self.tbl_curves.item(row, self.h_id)
                ti_id.setText(key)
                icon = self.parent().line_icon(self.parent().ui_curves[key]['color'] )
                ti = self.tbl_curves.item(row, self.h_chk)
                ti.setIcon(icon)
                ti.setCheckState(0)
            x_max = curve.x_max()
            x_min = curve.x_min()
            if x_min < 320.0 and x_max > 320.0:
                x_min = 320.0
            exp = 4.0
            ti_max = self.tbl_curves.item(row, self.h_x_max)
            ti_max.setText('{:.1f}'.format(x_max))
            ti_min = self.tbl_curves.item(row, self.h_x_min)
            ti_min.setText('{:.1f}'.format(x_min))
            ti_exp = self.tbl_curves.item(row, self.h_exp)
            ti_exp.setText('{:.2f}'.format(exp))
            params = self.get_scatter_params(key)
            a0, pc = params
            ti_offs = self.tbl_curves.item(row, self.h_offs)
            ti_offs.setText(str(a0)) #('{:.1g}'.format(a0))
            ti_amp = self.tbl_curves.item(row, self.h_amp)
            ti_amp.setText(str(pc)) #('{:.1g}'.format(pc)) 
        self.tbl_curves.resizeColumnsToContents()
        self.tbl_curves.resizeRowsToContents()
        
    def get_scatter_params(self, key):
        row = self.find_table_item_row(key)
        ti_min = self.tbl_curves.item(row, self.h_x_min)
        ti_max = self.tbl_curves.item(row, self.h_x_max)
        ti_exp = self.tbl_curves.item(row, self.h_exp)
        x_min = float(ti_min.text())
        x_max = float(ti_max.text())
        exp = float(ti_exp.text())
        curve = self.parent().curve_handler.curves[key]
        ps = curve.get_scatter_params(x_min, x_max, {'power': exp}, (0.0, 100.0))
        return ps
    
    def compute_scatter_contribution(self, key):
        row = self.find_table_item_row(key)
        ti_exp = self.tbl_curves.item(row, self.h_exp)
        ti_offs = self.tbl_curves.item(row, self.h_offs)
        ti_amp = self.tbl_curves.item(row, self.h_amp)
        a0 = float(ti_offs.text())
        c = float(ti_amp.text())
        exp = float(ti_exp.text())
        curve = self.parent().curve_handler.curves[key]
        func = curve.make_calc_scatter({'power': exp})
        scatter = func(curve.working_data['X'], *(a0, c))
        return scatter
    
    def plot_all(self):
        self.canvas.main_plot.cla()
        for row in range(self.tbl_curves.rowCount()):
            if self.tbl_curves.item(row, self.h_chk).checkState() == qt.Qt.Checked:
                key = self.tbl_curves.item(row, self.h_id).text()
                self.plot_result(key)
                
        x0, x1 = self.canvas.main_plot.get_xlim()
        y0, y1 = self.canvas.main_plot.get_ylim()
        x = x0 + 0.5 * (x1 - x0)
        y = y0 + 0.8 * (y1 - y0)
        self.canvas.main_plot.text(x, y, 
                'Dotted: original data\nDashed: scatter\nSolid: corrected')
        self.canvas.fig.canvas.draw()
    
    def plot_result(self, key):
        curve = self.parent().curve_handler.curves[key]
        clr = self.parent().ui_curves[key]['color']
        x = curve.working_data['X']
        y = curve.working_data['Y1']
        scatter = self.compute_scatter_contribution(key)
        y_corr = y - scatter
        self.canvas.main_plot.plot(x, scatter, ls='dashed', c=clr)
        self.canvas.main_plot.plot(x, y, ls='dotted', c=clr)
        self.canvas.main_plot.plot(x, y_corr, ls='solid', c=clr)
        
    def get_corrected_curve(self, key):
        curve = self.parent().curve_handler.curves[key]
        y = curve.working_data['Y1']
        scatter = self.compute_scatter_contribution(key)
        return y - scatter
    
    def set_scatter_correction(self):
        for row in range(self.tbl_curves.rowCount()):
            if self.tbl_curves.item(row, self.h_chk).checkState() == qt.Qt.Checked:
                key = self.tbl_curves.item(row, self.h_id).text()
                curve = self.parent().curve_handler.curves[key]
                corr = self.get_corrected_curve(key)
                curve.working_data['Y1'] = corr
        
    def find_table_item_row(self, key):
        items = self.tbl_curves.findItems(key, qt.Qt.MatchExactly)
        if len(items) > 0:
            return self.tbl_curves.row(items[0])
        return -1 

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False        
