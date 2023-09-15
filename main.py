import sys
from PyQt5.QtWidgets import QApplication, QDialog
from QT_Designer import login
import requests


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = login.Ui_Dialog()
        self.ui.setupUi(self)

        # 连接按钮的功能
        self.ui.confirmButton.clicked.connect(self.confirm)
        self.ui.cancelButton.clicked.connect(self.cancel)

        self.ui.ifSuccessButton.clicked.connect(self.if_success)
        self.ui.ifFailButton.clicked.connect(self.if_fail)

    # 获取各个输入框的内容
    def get_text(self):
        # 获取路径
        path = self.ui.pathInput.toPlainText()
        # 获取阈值
        yuzhi = self.ui.yuzhiInput.toPlainText()
        # 获取产品批号
        product_num = self.ui.productNumInput.toPlainText()
        # 获取工人工号
        person_num = self.ui.personNumInput.toPlainText()

        # self.ui.personNumInput.show()

    # 确认键
    def confirm(self):
        self.ui.inputCompleteLabel.setText("参数设定完毕，马上开始图像识别")
        self.ui.inputCompleteLabel_2.setText('开始运行图像识别算法：')

    # 取消键
    def cancel(self):
        self.ui.pathInput.clear()
        self.ui.personNumInput.clear()
        self.ui.yuzhiInput.clear()
        self.ui.productNumInput.clear()

    # 如果算法运行成功
    def if_success(self):
        self.ui.ifSuccessOrFailLabel.clear()
        self.ui.ifSuccessOrFailLabel.setText("图像算法运行成功，已保存到文件夹")

    # 如果算法运行失败
    def if_fail(self):
        self.ui.ifSuccessOrFailLabel.clear()
        self.ui.ifSuccessOrFailLabel.setText("图像算法运行失败，已保存到文件夹，请选择上报该问题")

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
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
