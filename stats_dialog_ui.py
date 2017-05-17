# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatsDialog(object):
    def setupUi(self, StatsDialog):
        StatsDialog.setObjectName("StatsDialog")
        StatsDialog.resize(282, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatsDialog.sizePolicy().hasHeightForWidth())
        StatsDialog.setSizePolicy(sizePolicy)
        StatsDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spectral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StatsDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(StatsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_stats = QtWidgets.QTableWidget(StatsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_stats.sizePolicy().hasHeightForWidth())
        self.tbl_stats.setSizePolicy(sizePolicy)
        self.tbl_stats.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbl_stats.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_stats.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tbl_stats.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tbl_stats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_stats.setDragDropOverwriteMode(False)
        self.tbl_stats.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_stats.setObjectName("tbl_stats")
        self.tbl_stats.setColumnCount(0)
        self.tbl_stats.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_stats)
        self.buttonBox = QtWidgets.QDialogButtonBox(StatsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StatsDialog)
        self.buttonBox.accepted.connect(StatsDialog.accept)
        self.buttonBox.rejected.connect(StatsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StatsDialog)

    def retranslateUi(self, StatsDialog):
        _translate = QtCore.QCoreApplication.translate
        StatsDialog.setWindowTitle(_translate("StatsDialog", "Curve statistics"))

import spectral_rc
