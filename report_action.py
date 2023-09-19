import os
import sys
from QT_Designer import report
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
from PIL import Image


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

        # self.Report_to_A_Button.clicked.connect(self.save_file_to_A_locally)
        # self.Report_to_B_Button.clicked.connect(self.save_file_to_B_locally)

        self.Report_to_A_Button.clicked.connect(lambda: self.save_file_locally("经理A"))
        self.Report_to_B_Button.clicked.connect(lambda: self.save_file_locally("经理B"))
        self.Report_to_C_Button.clicked.connect(lambda: self.save_file_locally("经理C"))

    def save_file_locally(self, manager_name):
        try:
            output_folder = "图片输出文件夹"
            output_path = os.path.join(output_folder, manager_name)

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # 打开图片
            input_image_path = "input.png"
            im = Image.open(input_image_path)

            # 保存图片到指定文件夹
            output_image_path = os.path.join(output_path, "output.png")
            im.save(output_image_path)

        except Exception as e:
            # 处理异常情况
            self.ReportOutputLabel.setText("保存文件时出现异常:", str(e))

        finally:
            self.ReportOutputLabel.setText('已经报告给' + manager_name)

