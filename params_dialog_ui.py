# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'params_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ParamsDialog(object):
    def setupUi(self, ParamsDialog):
        ParamsDialog.setObjectName("ParamsDialog")
        ParamsDialog.setWindowModality(QtCore.Qt.NonModal)
        ParamsDialog.resize(569, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ParamsDialog.sizePolicy().hasHeightForWidth())
        ParamsDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spectral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ParamsDialog.setWindowIcon(icon)
        ParamsDialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(ParamsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_params = QtWidgets.QTableWidget(ParamsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_params.sizePolicy().hasHeightForWidth())
        self.tbl_params.setSizePolicy(sizePolicy)
        self.tbl_params.setObjectName("tbl_params")
        self.tbl_params.setColumnCount(0)
        self.tbl_params.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_params)
        self.buttonBox = QtWidgets.QDialogButtonBox(ParamsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ParamsDialog)
        self.buttonBox.accepted.connect(ParamsDialog.accept)
        self.buttonBox.rejected.connect(ParamsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ParamsDialog)

    def retranslateUi(self, ParamsDialog):
        _translate = QtCore.QCoreApplication.translate
        ParamsDialog.setWindowTitle(_translate("ParamsDialog", "Parameters used for conversion"))

import spectral_rc
