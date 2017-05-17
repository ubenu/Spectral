# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scatter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScatterDialog(object):
    def setupUi(self, ScatterDialog):
        ScatterDialog.setObjectName("ScatterDialog")
        ScatterDialog.resize(627, 515)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spectral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScatterDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(ScatterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_view_all = QtWidgets.QCheckBox(ScatterDialog)
        self.chk_view_all.setObjectName("chk_view_all")
        self.verticalLayout.addWidget(self.chk_view_all)
        self.tbl_curves = QtWidgets.QTableWidget(ScatterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_curves.sizePolicy().hasHeightForWidth())
        self.tbl_curves.setSizePolicy(sizePolicy)
        self.tbl_curves.setMinimumSize(QtCore.QSize(0, 150))
        self.tbl_curves.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_curves.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tbl_curves.setObjectName("tbl_curves")
        self.tbl_curves.setColumnCount(0)
        self.tbl_curves.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_curves)
        self.mpl_window = QtWidgets.QWidget(ScatterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_window.sizePolicy().hasHeightForWidth())
        self.mpl_window.setSizePolicy(sizePolicy)
        self.mpl_window.setMinimumSize(QtCore.QSize(0, 350))
        self.mpl_window.setObjectName("mpl_window")
        self.mpl_layout = QtWidgets.QVBoxLayout(self.mpl_window)
        self.mpl_layout.setContentsMargins(0, 0, 0, 0)
        self.mpl_layout.setObjectName("mpl_layout")
        self.verticalLayout.addWidget(self.mpl_window)
        self.buttonBox = QtWidgets.QDialogButtonBox(ScatterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ScatterDialog)
        self.buttonBox.accepted.connect(ScatterDialog.accept)
        self.buttonBox.rejected.connect(ScatterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ScatterDialog)

    def retranslateUi(self, ScatterDialog):
        _translate = QtCore.QCoreApplication.translate
        ScatterDialog.setWindowTitle(_translate("ScatterDialog", "Scatter correction"))
        self.chk_view_all.setText(_translate("ScatterDialog", "View/hide all"))

import spectral_rc
