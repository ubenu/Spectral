# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:17:54 2017

@author: marietje
"""
#import pandas as pd

from PyQt5 import QtWidgets as widgets, QtCore as qt

import stats_dialog_ui as ui

#from PyQt5.uic import loadUiType
#Ui_StatsDialog, QDialog = loadUiType('stats_dialog.ui')

class StatsDialog(widgets.QDialog, ui.Ui_StatsDialog):

    def __init__(self, parent, data):
        super(widgets.QDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.set_all(data)
        
    def set_all(self, data):
        self.tbl_stats.setColumnCount(len(data.columns))
        self.tbl_stats.setRowCount(len(data.index.values))
        self.tbl_stats.setHorizontalHeaderLabels(data.columns.tolist())
        self.tbl_stats.setVerticalHeaderLabels(data.index.values.tolist())
        self.tbl_stats.verticalHeader().setDefaultAlignment(qt.Qt.AlignRight)


        for row in range(self.tbl_stats.rowCount()):
            for col in range(self.tbl_stats.columnCount()):
                ti = widgets.QTableWidgetItem()
                ti.setText('{:1.2g}'.format(data.iloc[row, col]))
                self.tbl_stats.setItem(row, col, ti)
            
        self.tbl_stats.resizeColumnsToContents()
        self.tbl_stats.resize(self.tbl_stats.sizeHint())

