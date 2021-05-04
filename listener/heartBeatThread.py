from time import ctime
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import socket


class HeartBeatListener(QtCore.QThread):
    # 定义信号
    receive_heartbeat_signal = pyqtSignal(str)

    def __init__(self):
        super(HeartBeatListener, self).__init__()
        # 全局参数配置
        self.encoding = "utf-8"
        self.broadcastPort = 9601
        # 创建广播接收器
        self.recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.recvSocket.bind(('', self.broadcastPort))
        print("------------------心跳报文监测线程开启---------------")

    def run(self):
        while True:
            receive_data = self.recvSocket.recvfrom(1024)
            print("\n-----------------------------------")
            print("收到心跳消息")
            receive_data_str = receive_data[0].decode(self.encoding)
            receive_data_ip = receive_data[1][0]
            print("心跳数据: time: %s || ip:port [%s : %s] || data: %s" % (
                ctime(), receive_data_ip, receive_data[1][1], receive_data[0].decode(self.encoding)))
            if receive_data_str[0:4] == "0312":
                self.receive_heartbeat_signal.emit(receive_data_str)
