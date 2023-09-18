import sys
from QT_Designer import report
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets


# 业务类需要继承两个类，一个设计的主界面，另一个是QMainWindow
class ReportActions(report.Ui_ReportWindow, QMainWindow):
    def __init__(self):
        """S
         特别注意（最容易出错）：
         1.派生新类访问基类需要super(),同时它的参数是基类文件下的类及“ui_home_window.py中的
           Ui_MainWindow类”，
        """
        super(report.Ui_ReportWindow, self).__init__()
        super().__init__()
        self.setupUi(self)
