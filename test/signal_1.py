from PyQt5.QtCore import *


# 自定义一个信号来触发事件
class MyTypeSignal(QObject):
    sendmsg = pyqtSignal(object)

    def run(self):
        self.sendmsg.emit("hello pyqt5")


class Myslot(QObject):
    def get(self, msg):
        print("message:"+ msg)


if __name__ == '__main__':
    send = MyTypeSignal()
    slot = Myslot()

    send.sendmsg.connect(slot.get)

    send.run()