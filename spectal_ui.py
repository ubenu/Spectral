# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectral.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1573, 982)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spectral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setProperty(".\\Resources", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.actionWidget = QtWidgets.QWidget(self.centralwidget)
        self.actionWidget.setObjectName("actionWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.actionWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grp_actions = QtWidgets.QGroupBox(self.actionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_actions.sizePolicy().hasHeightForWidth())
        self.grp_actions.setSizePolicy(sizePolicy)
        self.grp_actions.setObjectName("grp_actions")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.grp_actions)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_7 = QtWidgets.QGroupBox(self.grp_actions)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btn_open = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_open.setObjectName("btn_open")
        self.verticalLayout_11.addWidget(self.btn_open)
        self.btn_save_csv = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_save_csv.setObjectName("btn_save_csv")
        self.verticalLayout_11.addWidget(self.btn_save_csv)
        self.btn_save_cdpro = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_save_cdpro.setObjectName("btn_save_cdpro")
        self.verticalLayout_11.addWidget(self.btn_save_cdpro)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.grp_actions)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_hide = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_hide.sizePolicy().hasHeightForWidth())
        self.btn_hide.setSizePolicy(sizePolicy)
        self.btn_hide.setObjectName("btn_hide")
        self.verticalLayout_6.addWidget(self.btn_hide)
        self.btn_remove = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_remove.setObjectName("btn_remove")
        self.verticalLayout_6.addWidget(self.btn_remove)
        self.btn_reset = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_reset.setObjectName("btn_reset")
        self.verticalLayout_6.addWidget(self.btn_reset)
        self.btn_stats = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_stats.setObjectName("btn_stats")
        self.verticalLayout_6.addWidget(self.btn_stats)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.grp_actions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn_resample = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_resample.setObjectName("btn_resample")
        self.verticalLayout_10.addWidget(self.btn_resample)
        self.verticalLayout_5.addWidget(self.groupBox_6)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btn_convert = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_convert.setObjectName("btn_convert")
        self.verticalLayout_9.addWidget(self.btn_convert)
        self.rb_dAbs = QtWidgets.QRadioButton(self.groupBox_5)
        self.rb_dAbs.setChecked(True)
        self.rb_dAbs.setObjectName("rb_dAbs")
        self.verticalLayout_9.addWidget(self.rb_dAbs)
        self.rb_dEps_mrw = QtWidgets.QRadioButton(self.groupBox_5)
        self.rb_dEps_mrw.setObjectName("rb_dEps_mrw")
        self.verticalLayout_9.addWidget(self.rb_dEps_mrw)
        self.rb_dEps_M = QtWidgets.QRadioButton(self.groupBox_5)
        self.rb_dEps_M.setObjectName("rb_dEps_M")
        self.verticalLayout_9.addWidget(self.rb_dEps_M)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.grp_actions)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_scatter = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_scatter.setObjectName("btn_scatter")
        self.verticalLayout_7.addWidget(self.btn_scatter)
        self.btn_subtract_bl = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_subtract_bl.setObjectName("btn_subtract_bl")
        self.verticalLayout_7.addWidget(self.btn_subtract_bl)
        self.grp_smoothing = QtWidgets.QGroupBox(self.groupBox_3)
        self.grp_smoothing.setObjectName("grp_smoothing")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.grp_smoothing)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spin_smooth_window = QtWidgets.QDoubleSpinBox(self.grp_smoothing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_smooth_window.sizePolicy().hasHeightForWidth())
        self.spin_smooth_window.setSizePolicy(sizePolicy)
        self.spin_smooth_window.setDecimals(1)
        self.spin_smooth_window.setMinimum(0.1)
        self.spin_smooth_window.setMaximum(50.0)
        self.spin_smooth_window.setSingleStep(0.1)
        self.spin_smooth_window.setProperty("value", 5.0)
        self.spin_smooth_window.setObjectName("spin_smooth_window")
        self.gridLayout.addWidget(self.spin_smooth_window, 0, 0, 1, 1)
        self.lbl_smooth_window = QtWidgets.QLabel(self.grp_smoothing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_smooth_window.sizePolicy().hasHeightForWidth())
        self.lbl_smooth_window.setSizePolicy(sizePolicy)
        self.lbl_smooth_window.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_smooth_window.setObjectName("lbl_smooth_window")
        self.gridLayout.addWidget(self.lbl_smooth_window, 0, 1, 1, 1)
        self.spin_smooth_order = QtWidgets.QSpinBox(self.grp_smoothing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_smooth_order.sizePolicy().hasHeightForWidth())
        self.spin_smooth_order.setSizePolicy(sizePolicy)
        self.spin_smooth_order.setFrame(True)
        self.spin_smooth_order.setMaximum(5)
        self.spin_smooth_order.setProperty("value", 3)
        self.spin_smooth_order.setObjectName("spin_smooth_order")
        self.gridLayout.addWidget(self.spin_smooth_order, 1, 0, 1, 1)
        self.lbl_smooth_order = QtWidgets.QLabel(self.grp_smoothing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_smooth_order.sizePolicy().hasHeightForWidth())
        self.lbl_smooth_order.setSizePolicy(sizePolicy)
        self.lbl_smooth_order.setObjectName("lbl_smooth_order")
        self.gridLayout.addWidget(self.lbl_smooth_order, 1, 1, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout)
        self.btn_smooth = QtWidgets.QPushButton(self.grp_smoothing)
        self.btn_smooth.setObjectName("btn_smooth")
        self.verticalLayout_12.addWidget(self.btn_smooth)
        self.btn_deriv = QtWidgets.QPushButton(self.grp_smoothing)
        self.btn_deriv.setObjectName("btn_deriv")
        self.verticalLayout_12.addWidget(self.btn_deriv)
        self.verticalLayout_7.addWidget(self.grp_smoothing)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.grp_actions)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_math = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_math.setEnabled(True)
        self.btn_math.setObjectName("btn_math")
        self.verticalLayout_8.addWidget(self.btn_math)
        self.btn_copy = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_copy.setObjectName("btn_copy")
        self.verticalLayout_8.addWidget(self.btn_copy)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.grp_actions)
        self.grp_files = QtWidgets.QGroupBox(self.actionWidget)
        self.grp_files.setObjectName("grp_files")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grp_files)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chk_all_files = QtWidgets.QCheckBox(self.grp_files)
        self.chk_all_files.setObjectName("chk_all_files")
        self.verticalLayout_2.addWidget(self.chk_all_files)
        self.tbl_files = QtWidgets.QTableWidget(self.grp_files)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_files.sizePolicy().hasHeightForWidth())
        self.tbl_files.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tbl_files.setFont(font)
        self.tbl_files.setMouseTracking(True)
        self.tbl_files.setRowCount(0)
        self.tbl_files.setColumnCount(0)
        self.tbl_files.setObjectName("tbl_files")
        self.tbl_files.horizontalHeader().setStretchLastSection(True)
        self.tbl_files.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tbl_files)
        self.horizontalLayout.addWidget(self.grp_files)
        self.grp_plots = QtWidgets.QGroupBox(self.actionWidget)
        self.grp_plots.setObjectName("grp_plots")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grp_plots)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mpl_window = QtWidgets.QWidget(self.grp_plots)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_window.sizePolicy().hasHeightForWidth())
        self.mpl_window.setSizePolicy(sizePolicy)
        self.mpl_window.setObjectName("mpl_window")
        self.mpl_layout = QtWidgets.QVBoxLayout(self.mpl_window)
        self.mpl_layout.setContentsMargins(0, 0, 0, 0)
        self.mpl_layout.setObjectName("mpl_layout")
        self.verticalLayout.addWidget(self.mpl_window)
        self.horizontalLayout.addWidget(self.grp_plots)
        self.verticalLayout_4.addWidget(self.actionWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/mjs-open-data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon1)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/mjs_save_csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon2)
        self.action_save.setObjectName("action_save")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.action_quit.setObjectName("action_quit")
        self.action_save_cdpro = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/mjs_cdpro_input.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_cdpro.setIcon(icon3)
        self.action_save_cdpro.setObjectName("action_save_cdpro")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spectral"))
        self.grp_actions.setTitle(_translate("MainWindow", "Actions"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Input / Output"))
        self.btn_open.setText(_translate("MainWindow", "Open data"))
        self.btn_save_csv.setText(_translate("MainWindow", "Save as Csv (Excel)"))
        self.btn_save_cdpro.setText(_translate("MainWindow", "Save as CD Pro Input"))
        self.groupBox_2.setTitle(_translate("MainWindow", "General"))
        self.btn_hide.setText(_translate("MainWindow", "Hide / Show"))
        self.btn_remove.setText(_translate("MainWindow", "Remove"))
        self.btn_reset.setText(_translate("MainWindow", "Reset to original"))
        self.btn_stats.setText(_translate("MainWindow", "Statistics"))
        self.groupBox.setTitle(_translate("MainWindow", "Conversion"))
        self.groupBox_6.setTitle(_translate("MainWindow", "X-axis"))
        self.btn_resample.setText(_translate("MainWindow", "Resample X-axis"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Y-axis"))
        self.btn_convert.setText(_translate("MainWindow", "Convert"))
        self.rb_dAbs.setText(_translate("MainWindow", "Absorbance"))
        self.rb_dEps_mrw.setText(_translate("MainWindow", "Extinction (mrw)"))
        self.rb_dEps_M.setText(_translate("MainWindow", "Extinction (molar)"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Curve transformation"))
        self.btn_scatter.setText(_translate("MainWindow", "Remove scatter"))
        self.btn_subtract_bl.setText(_translate("MainWindow", "Subtract baseline"))
        self.grp_smoothing.setTitle(_translate("MainWindow", "Smoothing"))
        self.lbl_smooth_window.setText(_translate("MainWindow", "Window size"))
        self.lbl_smooth_order.setText(_translate("MainWindow", "Polynomial order"))
        self.btn_smooth.setText(_translate("MainWindow", "Smooth"))
        self.btn_deriv.setText(_translate("MainWindow", "Take derivative"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Curve creation"))
        self.btn_math.setText(_translate("MainWindow", "Combine multiple curves"))
        self.btn_copy.setText(_translate("MainWindow", "Copy"))
        self.grp_files.setTitle(_translate("MainWindow", "File Load"))
        self.chk_all_files.setText(_translate("MainWindow", "Check/uncheck all"))
        self.grp_plots.setTitle(_translate("MainWindow", "Plots"))
        self.action_open.setText(_translate("MainWindow", "Open data"))
        self.action_save.setText(_translate("MainWindow", "Save results"))
        self.action_save.setToolTip(_translate("MainWindow", "Save results in csv file"))
        self.action_quit.setText(_translate("MainWindow", "Quit"))
        self.action_save_cdpro.setText(_translate("MainWindow", "Save as CDPro Input File"))
        self.action_save_cdpro.setToolTip(_translate("MainWindow", "Save as CDPro Input file"))

import spectral_rc
