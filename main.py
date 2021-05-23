from PyQt5 import QtWidgets, QtCore
from fake_useragent import UserAgent
import requests
import sys

app = QtWidgets.QApplication(sys.argv)
timer = QtCore.QTimer()
label = QtWidgets.QLabel("")

label.setAlignment(QtCore.Qt.AlignHCenter)
label.resize(200, 30)

def main():
    try:
        browser = {"user-agent": UserAgent().random}
        response = requests.get("http://icanhazip.com/", headers=browser)
        label.setText("<h1 style='color:red'>{}</h1>".format(response.text))
    except:
        label.setText("<h1 style='color:red'>None</h1>")

timer.start(1000)
timer.timeout.connect(main)

label.move(960, 0)
label.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
label.setWindowFlag(QtCore.Qt.ToolTip)
label.show()
sys.exit(app.exec_())