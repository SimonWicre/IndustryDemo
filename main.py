import sys
from PyQt5.QtWidgets import *
from QT_Designer import login, report
import report_action
import requests


class MainWindow(login.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(login.Ui_MainWindow, self).__init__(parent)

        super().__init__()
        self.another_window = None
        self.setupUi(self)

        self.w = report.Ui_ReportWindow()
        # 连接按钮的功能
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.cancel)

        self.ifSuccessButton.clicked.connect(self.if_success)
        self.ifFailButton.clicked.connect(self.if_fail)

        # self.ifFailButton.clicked.connect(self.show_child)
        # self.child_window = report_action.ReportActions()

    # 获取各个输入框的内容
    def get_text(self):
        # 获取路径
        path = self.pathInput.toPlainText()
        # 获取阈值
        yuzhi = self.yuzhiInput.toPlainText()
        # 获取产品批号
        product_num = self.productNumInput.toPlainText()
        # 获取工人工号
        person_num = self.personNumInput.toPlainText()

        # self.ui.personNumInput.show()

    # 确认键
    def confirm(self):
        self.inputCompleteLabel.setText("参数设定完毕，马上开始图像识别")
        self.inputCompleteLabel_2.setText('开始运行图像识别算法：')

    # 取消键
    def cancel(self):
        self.pathInput.clear()
        self.personNumInput.clear()
        self.yuzhiInput.clear()
        self.productNumInput.clear()

    # 如果算法运行成功
    def if_success(self):
        self.ifSuccessOrFailLabel.clear()
        self.ifSuccessOrFailLabel.setText("图像算法运行成功，已保存到文件夹")

    # 如果算法运行失败
    def if_fail(self):
        self.ifSuccessOrFailLabel.clear()
        self.ifSuccessOrFailLabel.setText("图像算法运行失败，请选择上报该问题")

        self.another_window = report_action.ReportActions()
        self.another_window.show()

    # def show_child(self):
    #     self.child_window.show()


    # class Child(QWidget):
    #     def __init__(self):
    #         super().__init__()
    #         self.setWindowTitle("我是子窗口啊")

    # def queryWeather(self):
    #     cityName = self.ui.comboBox.currentText()
    #     cityCode = self.getCode(cityName)
    #
    #     r = requests.get("http://t.weather.sojson.com/api/weather/city/{}".format(cityCode))
    #
    #     print(r.json())
    #
    #     if r.json().get('status') == 200:
    #         weatherMsg = '城市：{}\n日期：{}\n天气：{}\nPM 2.5：{} {}\n温度：{}\n湿度：{}\n风力：{}\n\n{}'.format(
    #             r.json()['cityInfo']['city'],
    #             r.json()['data']['forecast'][0]['ymd'],
    #             r.json()['data']['forecast'][0]['type'],
    #             int(r.json()['data']['pm25']),
    #             r.json()['data']['quality'],
    #             r.json()['data']['wendu'],
    #             r.json()['data']['shidu'],
    #             r.json()['data']['forecast'][0]['fl'],
    #             r.json()['data']['forecast'][0]['notice'],
    #         )
    #     else:
    #         weatherMsg = '天气查询失败，请稍后再试！'
    #
    #     self.ui.textEdit.setText(weatherMsg)
    #
    # def getCode(self, cityName):
    #     cityDict = {"北京": "101010100",
    #                 "上海": "101020100",
    #                 "天津": "101030100"}
    #
    #     return cityDict.get(cityName, '101010100')

    def clearText(self):
        self.ui.pathInput.clear()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainWindow()
    myDlg.show()
    sys.exit(myapp.exec_())
