# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ifFailButton = QtWidgets.QPushButton(self.centralwidget)
        self.ifFailButton.setGeometry(QtCore.QRect(510, 680, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.ifFailButton.setFont(font)
        self.ifFailButton.setObjectName("ifFailButton")
        self.ifSuccessOrFailLabel = QtWidgets.QLabel(self.centralwidget)
        self.ifSuccessOrFailLabel.setGeometry(QtCore.QRect(140, 740, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.ifSuccessOrFailLabel.setFont(font)
        self.ifSuccessOrFailLabel.setText("")
        self.ifSuccessOrFailLabel.setObjectName("ifSuccessOrFailLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(190, 490, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.ifSuccessButton = QtWidgets.QPushButton(self.centralwidget)
        self.ifSuccessButton.setGeometry(QtCore.QRect(140, 680, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.ifSuccessButton.setFont(font)
        self.ifSuccessButton.setObjectName("ifSuccessButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(132, 152, 198, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.yuzhiInput = QtWidgets.QTextEdit(self.centralwidget)
        self.yuzhiInput.setGeometry(QtCore.QRect(337, 230, 453, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.yuzhiInput.setFont(font)
        self.yuzhiInput.setObjectName("yuzhiInput")
        self.personNumInput = QtWidgets.QTextEdit(self.centralwidget)
        self.personNumInput.setGeometry(QtCore.QRect(336, 384, 454, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.personNumInput.setFont(font)
        self.personNumInput.setObjectName("personNumInput")
        self.pathInput = QtWidgets.QTextEdit(self.centralwidget)
        self.pathInput.setGeometry(QtCore.QRect(336, 152, 453, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.pathInput.setFont(font)
        self.pathInput.setObjectName("pathInput")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(131, 307, 184, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 30, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.productNumInput = QtWidgets.QTextEdit(self.centralwidget)
        self.productNumInput.setGeometry(QtCore.QRect(336, 307, 454, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.productNumInput.setFont(font)
        self.productNumInput.setObjectName("productNumInput")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(131, 384, 184, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(520, 490, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(131, 230, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.inputCompleteLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.inputCompleteLabel_2.setGeometry(QtCore.QRect(140, 600, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.inputCompleteLabel_2.setFont(font)
        self.inputCompleteLabel_2.setText("")
        self.inputCompleteLabel_2.setObjectName("inputCompleteLabel_2")
        self.inputCompleteLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputCompleteLabel.setGeometry(QtCore.QRect(140, 560, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.inputCompleteLabel.setFont(font)
        self.inputCompleteLabel.setText("")
        self.inputCompleteLabel.setObjectName("inputCompleteLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ifFailButton.setText(_translate("MainWindow", "如果算法运行失败"))
        self.label_2.setText(_translate("MainWindow", "请设定参数：包括图像位置，阈值，产品批号，工人工号"))
        self.confirmButton.setText(_translate("MainWindow", "确认"))
        self.ifSuccessButton.setText(_translate("MainWindow", "如果算法运行成功"))
        self.label_3.setText(_translate("MainWindow", "请选择图像路径：  "))
        self.label_5.setText(_translate("MainWindow", "请输入产品批号："))
        self.label.setText(_translate("MainWindow", "*=*=*=*欢迎来到登陆系统页面*=*=*=*"))
        self.label_6.setText(_translate("MainWindow", "请输入工人工号："))
        self.cancelButton.setText(_translate("MainWindow", "取消"))
        self.label_4.setText(_translate("MainWindow", "请输入阈值：         "))
