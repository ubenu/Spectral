# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resample_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResampleDialog(object):
    def setupUi(self, ResampleDialog):
        ResampleDialog.setObjectName("ResampleDialog")
        ResampleDialog.resize(280, 92)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spectral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ResampleDialog.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ResampleDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(ResampleDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txt_start_x = QtWidgets.QLineEdit(ResampleDialog)
        self.txt_start_x.setObjectName("txt_start_x")
        self.gridLayout.addWidget(self.txt_start_x, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(ResampleDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txt_end_x = QtWidgets.QLineEdit(ResampleDialog)
        self.txt_end_x.setObjectName("txt_end_x")
        self.gridLayout.addWidget(self.txt_end_x, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(ResampleDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.txt_step_x = QtWidgets.QLineEdit(ResampleDialog)
        self.txt_step_x.setObjectName("txt_step_x")
        self.gridLayout.addWidget(self.txt_step_x, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ResampleDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ResampleDialog)
        self.buttonBox.accepted.connect(ResampleDialog.accept)
        self.buttonBox.rejected.connect(ResampleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ResampleDialog)

    def retranslateUi(self, ResampleDialog):
        _translate = QtCore.QCoreApplication.translate
        ResampleDialog.setWindowTitle(_translate("ResampleDialog", "X-axis parameters"))
        self.label.setText(_translate("ResampleDialog", "Start X"))
        self.label_2.setText(_translate("ResampleDialog", "End X"))
        self.label_3.setText(_translate("ResampleDialog", "X step"))

import spectral_rc
