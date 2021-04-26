import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)

class ThreadUpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("更新数据")
        self.resize(400, 200)
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(60, 100, 781, 381))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()

    def handleDisplay(self, data):
        self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ThreadUpdateUI()
    mainWindow.show()
    sys.exit(app.exec_())