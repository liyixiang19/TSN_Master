# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 909)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 40, 861, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.search_start = QtWidgets.QPushButton(self.frame)
        self.search_start.setGeometry(QtCore.QRect(20, 5, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.search_start.setFont(font)
        self.search_start.setObjectName("search_start")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 821, 121))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 55, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 280, 871, 126))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(20, 100, 831, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 50, 41, 49))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 51, 49))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(480, 50, 78, 49))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(270, 50, 39, 49))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(640, 50, 52, 49))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(770, 50, 52, 49))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(50, 410, 871, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 831, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_101 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_101.setText("")
        self.lineEdit_101.setObjectName("lineEdit_101")
        self.horizontalLayout.addWidget(self.lineEdit_101, 0, QtCore.Qt.AlignHCenter)
        self.line_11 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout.addWidget(self.line_11)
        self.lineEdit_102 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_102.setText("")
        self.lineEdit_102.setObjectName("lineEdit_102")
        self.horizontalLayout.addWidget(self.lineEdit_102, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.lineEdit_103 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_103.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_103.sizePolicy().hasHeightForWidth())
        self.lineEdit_103.setSizePolicy(sizePolicy)
        self.lineEdit_103.setText("")
        self.lineEdit_103.setObjectName("lineEdit_103")
        self.horizontalLayout.addWidget(self.lineEdit_103, 0, QtCore.Qt.AlignHCenter)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.lineEdit_104 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_104.sizePolicy().hasHeightForWidth())
        self.lineEdit_104.setSizePolicy(sizePolicy)
        self.lineEdit_104.setText("")
        self.lineEdit_104.setObjectName("lineEdit_104")
        self.horizontalLayout.addWidget(self.lineEdit_104, 0, QtCore.Qt.AlignHCenter)
        self.line_9 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout.addWidget(self.line_9)
        self.lineEdit_105 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_105.setText("")
        self.lineEdit_105.setObjectName("lineEdit_105")
        self.horizontalLayout.addWidget(self.lineEdit_105, 0, QtCore.Qt.AlignHCenter)
        self.line_4 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.pushButton_100 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_100.setObjectName("pushButton_100")
        self.horizontalLayout.addWidget(self.pushButton_100)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(50, 490, 881, 61))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.line_10 = QtWidgets.QFrame(self.frame_4)
        self.line_10.setGeometry(QtCore.QRect(20, 0, 841, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 831, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_201 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_201.setText("")
        self.lineEdit_201.setObjectName("lineEdit_201")
        self.horizontalLayout_2.addWidget(self.lineEdit_201, 0, QtCore.Qt.AlignHCenter)
        self.line_12 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_2.addWidget(self.line_12)
        self.lineEdit_202 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_202.setText("")
        self.lineEdit_202.setObjectName("lineEdit_202")
        self.horizontalLayout_2.addWidget(self.lineEdit_202, 0, QtCore.Qt.AlignHCenter)
        self.line_5 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.lineEdit_203 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_203.sizePolicy().hasHeightForWidth())
        self.lineEdit_203.setSizePolicy(sizePolicy)
        self.lineEdit_203.setText("")
        self.lineEdit_203.setObjectName("lineEdit_203")
        self.horizontalLayout_2.addWidget(self.lineEdit_203, 0, QtCore.Qt.AlignHCenter)
        self.line_6 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.lineEdit_204 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_204.sizePolicy().hasHeightForWidth())
        self.lineEdit_204.setSizePolicy(sizePolicy)
        self.lineEdit_204.setText("")
        self.lineEdit_204.setObjectName("lineEdit_204")
        self.horizontalLayout_2.addWidget(self.lineEdit_204, 0, QtCore.Qt.AlignHCenter)
        self.line_8 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_2.addWidget(self.line_8)
        self.lineEdit_205 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_205.setText("")
        self.lineEdit_205.setObjectName("lineEdit_205")
        self.horizontalLayout_2.addWidget(self.lineEdit_205, 0, QtCore.Qt.AlignHCenter)
        self.line_7 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.pushButton_200 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_200.setObjectName("pushButton_200")
        self.horizontalLayout_2.addWidget(self.pushButton_200)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(50, 570, 881, 61))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.line_18 = QtWidgets.QFrame(self.frame_5)
        self.line_18.setGeometry(QtCore.QRect(20, 0, 841, 16))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 831, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_301 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_301.setText("")
        self.lineEdit_301.setObjectName("lineEdit_301")
        self.horizontalLayout_4.addWidget(self.lineEdit_301, 0, QtCore.Qt.AlignHCenter)
        self.line_13 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_4.addWidget(self.line_13)
        self.lineEdit_302 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_302.setText("")
        self.lineEdit_302.setObjectName("lineEdit_302")
        self.horizontalLayout_4.addWidget(self.lineEdit_302, 0, QtCore.Qt.AlignHCenter)
        self.line_14 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayout_4.addWidget(self.line_14)
        self.lineEdit_303 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_303.sizePolicy().hasHeightForWidth())
        self.lineEdit_303.setSizePolicy(sizePolicy)
        self.lineEdit_303.setText("")
        self.lineEdit_303.setObjectName("lineEdit_303")
        self.horizontalLayout_4.addWidget(self.lineEdit_303, 0, QtCore.Qt.AlignHCenter)
        self.line_15 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.horizontalLayout_4.addWidget(self.line_15)
        self.lineEdit_304 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_304.sizePolicy().hasHeightForWidth())
        self.lineEdit_304.setSizePolicy(sizePolicy)
        self.lineEdit_304.setText("")
        self.lineEdit_304.setObjectName("lineEdit_304")
        self.horizontalLayout_4.addWidget(self.lineEdit_304, 0, QtCore.Qt.AlignHCenter)
        self.line_16 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.horizontalLayout_4.addWidget(self.line_16)
        self.lineEdit_305 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_305.setText("")
        self.lineEdit_305.setObjectName("lineEdit_305")
        self.horizontalLayout_4.addWidget(self.lineEdit_305, 0, QtCore.Qt.AlignHCenter)
        self.line_17 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.horizontalLayout_4.addWidget(self.line_17)
        self.pushButton_300 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_300.setObjectName("pushButton_300")
        self.horizontalLayout_4.addWidget(self.pushButton_300)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(50, 670, 881, 211))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.motion_control = QtWidgets.QPushButton(self.frame_6)
        self.motion_control.setGeometry(QtCore.QRect(10, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.motion_control.setFont(font)
        self.motion_control.setObjectName("motion_control")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setGeometry(QtCore.QRect(180, 70, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 120, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(380, 60, 191, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.run_mode_1 = QtWidgets.QPushButton(self.frame_6)
        self.run_mode_1.setGeometry(QtCore.QRect(620, 72, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.run_mode_1.setFont(font)
        self.run_mode_1.setObjectName("run_mode_1")
        self.run_mode_2 = QtWidgets.QPushButton(self.frame_6)
        self.run_mode_2.setGeometry(QtCore.QRect(620, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.run_mode_2.setFont(font)
        self.run_mode_2.setObjectName("run_mode_2")
        self.run_mode_3 = QtWidgets.QPushButton(self.frame_6)
        self.run_mode_3.setGeometry(QtCore.QRect(620, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.run_mode_3.setFont(font)
        self.run_mode_3.setObjectName("run_mode_3")
        self.line_19 = QtWidgets.QFrame(self.frame_6)
        self.line_19.setGeometry(QtCore.QRect(10, 50, 831, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.frame_6)
        self.line_20.setGeometry(QtCore.QRect(360, 60, 20, 131))
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.frame_6)
        self.line_21.setGeometry(QtCore.QRect(0, 190, 831, 16))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_start.setText(_translate("MainWindow", "搜索从站"))
        self.label.setText(_translate("MainWindow", "收到的数据"))
        self.pushButton_3.setText(_translate("MainWindow", "从站列表"))
        self.label_8.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "类型"))
        self.label_5.setText(_translate("MainWindow", "IP地址"))
        self.label_3.setText(_translate("MainWindow", "VID"))
        self.label_4.setText(_translate("MainWindow", "状态"))
        self.label_7.setText(_translate("MainWindow", "操作"))
        self.pushButton_100.setText(_translate("MainWindow", "设置"))
        self.pushButton_200.setText(_translate("MainWindow", "设置"))
        self.pushButton_300.setText(_translate("MainWindow", "设置"))
        self.motion_control.setText(_translate("MainWindow", "运动控制"))
        self.label_9.setText(_translate("MainWindow", "选择控制节点："))
        self.label_6.setText(_translate("MainWindow", "选择同步运动模式："))
        self.run_mode_1.setText(_translate("MainWindow", "MODE 1"))
        self.run_mode_2.setText(_translate("MainWindow", "MODE 2"))
        self.run_mode_3.setText(_translate("MainWindow", "MODE 3"))
