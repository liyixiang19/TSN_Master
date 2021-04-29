import time
from time import ctime
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import socket


class ReceiveThread(QtCore.QThread):
    receive_signal = pyqtSignal(str, str)
    query_result_signal = pyqtSignal(str)
    real_time_data_signal = pyqtSignal(str)

    def __init__(self):
        super(ReceiveThread, self).__init__()
        # 全局参数配置
        self.encoding = "utf-8"
        self.broadcastPort = 9000
        # 创建广播接收器
        self.recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.recvSocket.bind(('', self.broadcastPort))

    def run(self):
        while True:
            receive_data = self.recvSocket.recvfrom(1024)
            print("\n-----------------接收到从站广播信号-------------------")
            receive_data_str = receive_data[0].decode(self.encoding)
            receive_data_ip = receive_data[1][0]
            print("接收到的数据: time: %s || ip:port [%s : %s] || data: %s" % (
                ctime(), receive_data_ip, receive_data[1][1], receive_data[0].decode(self.encoding)))
            # 触发信号
            if receive_data_str[0:4] == "0812":
                self.receive_signal.emit(receive_data_str, receive_data_ip)
            if receive_data_str[0:4] == "0715":
                query_res = receive_data_str[32:36]
                if receive_data_str[12:16] == "9988":
                    self.real_time_data_signal.emit(query_res)
                else:
                    # 查询指令返回消息
                    self.query_result_signal.emit(query_res)


class HeartBeatListener(QtCore.QThread):
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


