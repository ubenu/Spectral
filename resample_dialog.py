# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:18:13 2017

@author: schilsm
"""
import numpy as np, copy as cp

from PyQt5 import QtWidgets as widgets

import resample_dialog_ui as ui

#from PyQt5.uic import loadUiType
#Ui_ResampleDialog, QDialog = loadUiType('resample_dialog.ui')

class ResampleDialog(widgets.QDialog, ui.Ui_ResampleDialog):

    values = range(3)
    [x_start, x_end, x_step] = values
    
    def __init__(self, parent, x_start, x_end, x_step):
        super(widgets.QDialog, self).__init__(parent)
        self.setupUi(self)
        self.original_values = np.zeros((3)) 
        v = np.array([x_start, x_end, x_step])
        np.around(v, decimals=3, out=self.original_values)
        self.values = cp.deepcopy(self.original_values)
        self.set_all()
        
    def set_all(self):
        self.txt_start_x.setText(str(self.values[self.x_start]))        
        self.txt_end_x.setText(str(self.values[self.x_end]))
        self.txt_step_x.setText(str(self.values[self.x_step]))
        
    def get_values(self):
        return self.values
    
    def accept(self):
        class XStartError(Exception): 
            pass
        class XEndError(Exception): 
            pass
        class XStepError(Exception): 
            pass
        
        x_start = float(self.txt_start_x.text())
        x_end = float(self.txt_end_x.text())
        x_step = float(self.txt_step_x.text())
        proposed = np.zeros((3))
        np.around(np.array([x_start, x_end, x_step]), decimals=3, out=proposed)
        xxb = self.original_values[self.x_start] 
        xxe = self.original_values[self.x_end] 
        
        try:
            if proposed[self.x_start] < xxb or proposed[self.x_start] > xxe:
                raise XStartError(
                        "Start X must be between {:} and {:}".format(xxb, xxe)
                        )
            if proposed[self.x_end] < xxb or proposed[self.x_end] > xxe:
                raise XEndError(
                        "End X must be between {:} and {:}".format(xxb, xxe)
                        )
            if proposed[self.x_end] <= proposed[self.x_start]:
                raise XEndError(
                        "End X must be greater than start X".format()
                        )
            if proposed[self.x_step] > (
                    proposed[self.x_end]-proposed[self.x_start] ):
                raise XStepError(
                        "Step X must be smaller than {:}".format(
                                proposed[self.x_end]-proposed[self.x_start] )
                        )
        except XStartError as e:
            widgets.QMessageBox.warning(self, "Error on limits", str(e))
            self.txt_start_x.selectAll()
            self.txt_start_x.setFocus()
            return
        except XEndError as e:
            widgets.QMessageBox.warning(self, "Error on limits", str(e))
            self.txt_end_x.selectAll()
            self.txt_end_x.setFocus()
            return
        except XStepError as e:
            widgets.QMessageBox.warning(self, "Error on step", str(e))
            self.txt_step_x.selectAll()
            self.txt_step_x.setFocus()
            return
 
        self.values = proposed
        widgets.QDialog.accept(self)