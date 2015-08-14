# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(653, 406)
        self.widget = QtGui.QWidget(MainWindow)
        self.widget.setMinimumSize(QtCore.QSize(400, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.frame = QtGui.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(-1, 20, 311, 301))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setMargin(0)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.ipSetting = QtGui.QLineEdit(self.frame)
        self.ipSetting.setObjectName(_fromUtf8("ipSetting"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.ipSetting)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.portSetting = QtGui.QLineEdit(self.frame)
        self.portSetting.setObjectName(_fromUtf8("portSetting"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.portSetting)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.mbitCombo = QtGui.QComboBox(self.frame)
        self.mbitCombo.setObjectName(_fromUtf8("mbitCombo"))
        self.mbitCombo.addItem(_fromUtf8(""))
        self.mbitCombo.addItem(_fromUtf8(""))
        self.mbitCombo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.mbitCombo)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtGui.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(320, 20, 301, 301))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.resolutionSetting = QtGui.QComboBox(self.frame_2)
        self.resolutionSetting.setObjectName(_fromUtf8("resolutionSetting"))
        self.resolutionSetting.addItem(_fromUtf8(""))
        self.resolutionSetting.addItem(_fromUtf8(""))
        self.resolutionSetting.addItem(_fromUtf8(""))
        self.resolutionSetting.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.resolutionSetting)
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.fpsSetting = QtGui.QComboBox(self.frame_2)
        self.fpsSetting.setObjectName(_fromUtf8("fpsSetting"))
        self.fpsSetting.addItem(_fromUtf8(""))
        self.fpsSetting.addItem(_fromUtf8(""))
        self.fpsSetting.addItem(_fromUtf8(""))
        self.fpsSetting.addItem(_fromUtf8(""))
        self.fpsSetting.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.fpsSetting)
        self.start_button = QtGui.QPushButton(self.frame_2)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.formLayout_3.setWidget(12, QtGui.QFormLayout.FieldRole, self.start_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_3.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.frame_3 = QtGui.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 301, 331))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 331))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.bitrate_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.bitrate_edit.setObjectName(_fromUtf8("bitrate_edit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.bitrate_edit)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.max_bitrate_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.max_bitrate_edit.setObjectName(_fromUtf8("max_bitrate_edit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.max_bitrate_edit)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.slice_max_size_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.slice_max_size_edit.setObjectName(_fromUtf8("slice_max_size_edit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.slice_max_size_edit)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.advancedButton = QtGui.QPushButton(self.widget)
        self.advancedButton.setObjectName(_fromUtf8("advancedButton"))
        self.gridLayout.addWidget(self.advancedButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.widget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 653, 29))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.mbitCombo.setCurrentIndex(2)
        self.resolutionSetting.setCurrentIndex(1)
        self.fpsSetting.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Ağ Ayarları", None))
        self.label_7.setText(_translate("MainWindow", "Ip", None))
        self.ipSetting.setText(_translate("MainWindow", "192.168.42.1", None))
        self.label_8.setText(_translate("MainWindow", "Port", None))
        self.portSetting.setText(_translate("MainWindow", "1234", None))
        self.label_5.setText(_translate("MainWindow", "mbps", None))
        self.mbitCombo.setItemText(0, _translate("MainWindow", "5", None))
        self.mbitCombo.setItemText(1, _translate("MainWindow", "10", None))
        self.mbitCombo.setItemText(2, _translate("MainWindow", "20", None))
        self.label.setText(_translate("MainWindow", "Görüntü Ayarları", None))
        self.label_3.setText(_translate("MainWindow", "Çözünürlük", None))
        self.resolutionSetting.setItemText(0, _translate("MainWindow", "800x600", None))
        self.resolutionSetting.setItemText(1, _translate("MainWindow", "1024x768", None))
        self.resolutionSetting.setItemText(2, _translate("MainWindow", "1280x720", None))
        self.resolutionSetting.setItemText(3, _translate("MainWindow", "1280x800", None))
        self.label_4.setText(_translate("MainWindow", "FPS", None))
        self.fpsSetting.setItemText(0, _translate("MainWindow", "10", None))
        self.fpsSetting.setItemText(1, _translate("MainWindow", "15", None))
        self.fpsSetting.setItemText(2, _translate("MainWindow", "20", None))
        self.fpsSetting.setItemText(3, _translate("MainWindow", "25", None))
        self.fpsSetting.setItemText(4, _translate("MainWindow", "30", None))
        self.start_button.setText(_translate("MainWindow", "Başlat", None))
        self.label_6.setText(_translate("MainWindow", "BITRATE ", None))
        self.bitrate_edit.setText(_translate("MainWindow", "12000", None))
        self.label_9.setText(_translate("MainWindow", "MAX_BITRATE", None))
        self.max_bitrate_edit.setText(_translate("MainWindow", "18000", None))
        self.label_10.setText(_translate("MainWindow", "SLICE_MAX_SIZE", None))
        self.slice_max_size_edit.setText(_translate("MainWindow", "15000", None))
        self.advancedButton.setText(_translate("MainWindow", "Gelişmiş", None))

