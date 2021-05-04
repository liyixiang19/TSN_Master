import sys
import time
import socket
from PyQt5 import QtGui
from qtpy import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow

from common import glo
from ui import designer, new_designer
import listener.heartBeatThread
import listener.receiveThread
import survive.heartBeat


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = designer.Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.initUI()
        # 心跳计时器线程
        self.heartbeatTimerThread = survive.heartBeat.HeartBeatTimerThread()
        # 心跳线程
        self.heartBeatThread = listener.heartBeatThread.HeartBeatListener()
        # 监听消息线程
        self.recvThread = listener.receiveThread.ReceiveThread()
        # 连接槽函数
        self.heartbeatTimerThread.offline_signal.connect(self.offlineHandler)
        self.heartBeatThread.receive_heartbeat_signal.connect(self.heartbeatHandler)
        self.recvThread.receive_signal.connect(self.displayHandler)
        self.recvThread.query_result_signal.connect(self.queryResultHandler)
        self.recvThread.real_time_data_signal.connect(self.realtimeDataHandler)
        # 控制功能选择的节点
        self.node_dict = {}
        # 创建广播发送器
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # 定义变量
        self.slave_to_master = "0812"
        self.master_to_slave = "0827"
        self.control_type = "0625"
        self.control_port = 8000
        self.mode_dict = {1: "2301", 2: "2302", 3: "2303"}
        self.fake_vid = "0000000000000000"

    def initUI(self):
        self.main_ui.textEdit.setText("返回内容:")

    @pyqtSlot()
    def on_search_start_clicked(self):
        print("点击了搜索从站按钮,开启监听线程...")
        # 实例化组网报文监测
        # 开启消息监听线程
        self.recvThread.start()
        # 启动心跳报文监测线程
        self.heartBeatThread.start()
        # 点击功能屏蔽
        self.main_ui.search_start.setDisabled(True)

    @pyqtSlot()
    def on_motion_control_clicked(self):
        print("点击了运动控制按钮，开启运动控制功能...")
        if 1001 != glo.get_value("deviceId"):
            cur_device_id = glo.get_value("deviceId")
            # 添加当前设备id到combobox选项中
            for i in range(1001, cur_device_id):
                self.main_ui.comboBox.addItem(str(i))
                self.main_ui.comboBox_2.addItem(str(i))
        else:
            print("未发现活跃的从站设备...")
            QMessageBox.information(self, '信息提示对话框', "未发现活跃的从站设备！")

    def clickEvent(self, flag):
        if self.main_ui.comboBox.currentText() == "":
            print("请先打开控制功能，选择要操作的从站节点！")
            QMessageBox.information(self, '信息提示对话框', "请先打开控制功能，选择要操作的从站节点！")
        else:
            # 获取控制的节点
            node_1 = self.main_ui.comboBox.currentText()
            node_2 = self.main_ui.comboBox_2.currentText()
            if node_1 == node_2:
                # 组装消息帧，发送给控制端口
                run_data = self.control_type + "0001" + node_1 + self.mode_dict[flag] + self.fake_vid
                print("发送的控制指令：", run_data, "\n")
                self.sendSocket.sendto(run_data.encode("utf-8"), ("255.255.255.255", self.control_port))
            else:
                # 组装消息帧，发送给控制端口
                run_data_1 = self.control_type + "0001" + node_1 + self.mode_dict[flag] + self.fake_vid
                self.sendSocket.sendto(run_data_1.encode("utf-8"), ("255.255.255.255", self.control_port))
                run_data_2 = self.control_type + "0001" + node_1 + self.mode_dict[flag] + self.fake_vid
                self.sendSocket.sendto(run_data_2.encode("utf-8"), ("255.255.255.255", self.control_port))

    @pyqtSlot()
    def on_run_mode_1_clicked(self):
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>启动运动模式1<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        self.clickEvent(1)

    @pyqtSlot()
    def on_run_mode_2_clicked(self):
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>启动运动模式2<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        # 组装消息帧，发送给控制端口
        self.clickEvent(2)

    @pyqtSlot()
    def on_run_mode_3_clicked(self):
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>启动运动模式3<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        # 组装消息帧，发送给控制端口
        self.clickEvent(3)

    @pyqtSlot()
    def on_set_button_1001_clicked(self):
        glo.set_value("set_button_id", "1001")

    @pyqtSlot()
    def on_set_button_1002_clicked(self):
        glo.set_value("set_button_id", "1002")

    @pyqtSlot()
    def on_set_button_1003_clicked(self):
        glo.set_value("set_button_id", "1003")

    def displayHandler(self, msg, ip):
        print("【组网信号槽函数触发】")
        if 200 == self.judgeData(msg, ip):
            print("收到从站组网请求，请求正确，成功返回数据, 设备入网成功")
            self.main_ui.textEdit.append(str(msg))
        print("-------------------------------------\n")

    def heartbeatHandler(self, msg):
        print("【心跳信号槽函数触发】")
        if 200 == self.judgeAliveMsg(msg):
            print("从站心跳信号，请求正确，操作完成")
        print("-----------------------------------\n")

    def offlineHandler(self, de_id):
        print("【设备离线信号槽函数触发】")
        print(">>>>>>>>>>>进行离线操作<<<<<<<<<<")
        node_status = "offline"
        if de_id == "1001":
            self.main_ui.lineEdit_105.setText(node_status)
            palette = self.main_ui.lineEdit_105.palette()
            palette.setColor(QtGui.QPalette.Base, QtCore.Qt.red)
            self.main_ui.lineEdit_105.setPalette(palette)
            self.main_ui.lineEdit_105.setAutoFillBackground(True)
            self.main_ui.set_button_1001.setDisabled(True)
        elif de_id == "1002":
            self.main_ui.lineEdit_205.setText(node_status)
            palette = self.main_ui.lineEdit_205.palette()
            palette.setColor(QtGui.QPalette.Base, QtCore.Qt.red)
            self.main_ui.lineEdit_205.setPalette(palette)
            self.main_ui.lineEdit_205.setAutoFillBackground(True)
            self.main_ui.set_button_1002.setDisabled(True)
        elif de_id == "1003":
            self.main_ui.lineEdit_305.setText(node_status)
            palette = self.main_ui.lineEdit_305.palette()
            palette.setColor(QtGui.QPalette.Base, QtCore.Qt.red)
            self.main_ui.lineEdit_305.setPalette(palette)
            self.main_ui.lineEdit_305.setAutoFillBackground(True)
            self.main_ui.set_button_1003.setDisabled(True)
        else:
            print("设备id错误，请检查")
        print("-------------------------------------\n")

    def queryResultHandler(self, res):
        print("【查询数据信号槽函数触发】")
        print("receiving: ", res)
        childWin.child.query_result_data.setText(res)
        print("-------------------------------------\n")

    def realtimeDataHandler(self, res):
        print("【实时数据信号槽函数触发】")
        print("receiving: ", res)
        childWin.child.show_realtime_data.setText(res)
        print("-------------------------------------\n")

    def judgeData(self, data, ip):
        print("解析数据: " + data)
        if self.slave_to_master == data[0:4]:
            print("协议格式正确! 正在配置从站...")
            organization_status = "0200"
            # 解析数据
            num = glo.get_value("deviceId")
            device_id = str(num)
            device_type = data[4:8]
            device_info = data[8:12]
            device_status = data[12:16]
            device_vid = data[16:32]
            print(device_vid)
            print(self.node_dict)
            if device_vid in self.node_dict.keys():
                print("该设备已入网.....")
            else:
                self.node_dict[device_vid] = device_id
                # 组装数据帧并返回
                response_data = self.master_to_slave + organization_status + device_id + device_status + device_vid
                print("返回给从站的响应数据为: " + response_data)
                time.sleep(2)
                self.sendSocket.sendto(response_data.encode("utf-8"), ("255.255.255.255", 8000))
                print("设备入网配置完成，设备类型: %s || 设备ID: %s || 设备信息: %s || 设备VID: %s" % (
                    device_type, device_id, device_info, device_vid))
                # 入网成功、显示在从站列表中，设置line text
                self.showList(device_id, device_type, device_vid, ip, device_status)
                # 保存实例
                glo.set_value(device_id, True)
                # 启动心跳线程，创建一个timer
                self.heartbeatTimerThread.start()
                # 设备入网id自增
                glo.set_value("deviceId", num + 1)
                return 200
        else:
            print("错误的数据格式，请检查...")
            return 300

    def judgeAliveMsg(self, data):
        if "0312" == data[0:4]:
            # 解析数据
            alive_device_id = data[32:36]
            alive_device_type = data[4:8]
            alive_device_info = data[8:12]
            # 设备状态
            alive_device_status = data[12:16]
            alive_device_vid = data[16:32]
            if alive_device_status == "0200":
                alive_status = "online"
                # 判断设备状态，用于重置alive标志位
                print("心跳报文信息解析，设备类型: %s || 设备ID: %s || 设备信息: %s || 设备VID: %s ======== status：【%s】" % (
                    alive_device_type, alive_device_id, alive_device_info, alive_device_vid, alive_status))
            if glo.get_value(alive_device_id) != 400:
                glo.set_value(alive_device_id, True)
                return 200
        else:
            print("错误的数据格式，请检查...")
            return 300

    def showList(self, d_id, d_type, vid, ip, status):
        print("界面显示的数据: ", d_id, d_type, vid, ip, status)
        if d_id == "1001":
            self.main_ui.lineEdit_101.setText(d_id)
            self.main_ui.lineEdit_102.setText(d_type)
            self.main_ui.lineEdit_103.setText(vid)
            self.main_ui.lineEdit_104.setText(ip)
            if status == "0001":
                self.main_ui.lineEdit_105.setText("online")
                palette = self.main_ui.lineEdit_105.palette()
                palette.setColor(QtGui.QPalette.Base, QtCore.Qt.green)
                self.main_ui.lineEdit_105.setPalette(palette)
                self.main_ui.lineEdit_105.setAutoFillBackground(True)
                self.main_ui.set_button_1001.setDisabled(False)
            else:
                self.main_ui.lineEdit_105.setText("unknown")
        elif d_id == "1002":
            self.main_ui.lineEdit_201.setText(d_id)
            self.main_ui.lineEdit_202.setText(d_type)
            self.main_ui.lineEdit_203.setText(vid)
            self.main_ui.lineEdit_204.setText(ip)
            if status == "0001":
                self.main_ui.lineEdit_205.setText("online")
                palette = self.main_ui.lineEdit_205.palette()
                palette.setColor(QtGui.QPalette.Base, QtCore.Qt.green)
                self.main_ui.lineEdit_205.setPalette(palette)
                self.main_ui.lineEdit_205.setAutoFillBackground(True)
                self.main_ui.set_button_1002.setDisabled(False)
            else:
                self.main_ui.lineEdit_105.setText("unknown")
        elif d_id == "1003":
            self.main_ui.lineEdit_301.setText(d_id)
            self.main_ui.lineEdit_302.setText(d_type)
            self.main_ui.lineEdit_303.setText(vid)
            self.main_ui.lineEdit_304.setText(ip)
            if status == "0001":
                self.main_ui.lineEdit_305.setText("online")
                palette = self.main_ui.lineEdit_305.palette()
                palette.setColor(QtGui.QPalette.Base, QtCore.Qt.green)
                self.main_ui.lineEdit_305.setPalette(palette)
                self.main_ui.lineEdit_305.setAutoFillBackground(True)
                self.main_ui.set_button_1003.setDisabled(False)
            else:
                self.main_ui.lineEdit_105.setText("unknown")


class ChildWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = new_designer.Ui_ChildWindow()
        self.child.setupUi(self)
        self.query_type = "0714"
        self.query_realtime_type = "0716"
        self.set_type = "0861"
        self.fake_vid = "0000000000000000"

        # 创建广播发送器
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # 定义变量
        self.query_port = 8000
        self.velocity = "1011"
        self.plus = "1012"
        self.position = "1013"

    @pyqtSlot()
    def on_set_button_clicked(self):
        set_button_id = glo.get_value("set_button_id")
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>设置从站==【%s】<<<<<<<<<<<<<<<<<<<<<<<<<<<" % set_button_id)
        velocity = self.child.velocity.text()
        position = self.child.position.text()
        plus = self.child.plus.text()
        print(velocity, plus, position)
        # 校验速度
        if velocity != "":
            velocity = velocity.zfill(4)
            query_velocity_data = self.set_type + "0001" + set_button_id + self.velocity + self.fake_vid + velocity
            print("发送的控制指令：", query_velocity_data, "\n")
            self.sendSocket.sendto(query_velocity_data.encode("utf-8"), ("255.255.255.255", self.query_port))
            # 速度
        if position != "":
            position = position.zfill(4)
            query_position_data = self.set_type + "0001" + set_button_id + self.position + self.fake_vid + position
            print("发送的控制指令：", query_position_data, "\n")
            self.sendSocket.sendto(query_position_data.encode("utf-8"), ("255.255.255.255", self.query_port))
            # 速度
        if plus != "":
            plus = plus.zfill(4)
            query_plus_data = self.set_type + "0001" + set_button_id + self.plus + self.fake_vid + plus
            print("发送的控制指令：", query_plus_data, "\n")
            self.sendSocket.sendto(query_plus_data.encode("utf-8"), ("255.255.255.255", self.query_port))

    @pyqtSlot()
    def on_realtime_data_clicked(self):
        set_button_id = glo.get_value("set_button_id")
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>实时监测从站数据==【%s】<<<<<<<<<<<<<<<<<<<<<<<<<<<" % set_button_id)
        query_realtime_position_data = self.query_realtime_type + "0001" + set_button_id + self.position \
                                       + self.fake_vid
        print("发送的实时数据监测指令：", query_realtime_position_data, "\n")
        self.sendSocket.sendto(query_realtime_position_data.encode("utf-8"), ("255.255.255.255", self.query_port))

    @pyqtSlot()
    def on_query_button_clicked(self):
        set_button_id = glo.get_value("set_button_id")
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>查询从站==【%s】<<<<<<<<<<<<<<<<<<<<<<<<<<<" % set_button_id)
        query = self.child.query_type.currentText()
        print("查询类型：", query)
        if query == "速度":
            query_velocity_data = self.query_type + "0001" + set_button_id + self.velocity + self.fake_vid
            print("发送的查询指令：", query_velocity_data, "\n")
            self.sendSocket.sendto(query_velocity_data.encode("utf-8"), ("255.255.255.255", self.query_port))
        if query == "位置":
            query_position_data = self.query_type + "0001" + set_button_id + self.position + self.fake_vid
            print("发送的查询指令：", query_position_data, "\n")
            self.sendSocket.sendto(query_position_data.encode("utf-8"), ("255.255.255.255", self.query_port))
        if query == "脉冲数":
            query_plus_data = self.query_type + "0001" + set_button_id + self.plus + self.fake_vid
            print("发送的查询指令：", query_plus_data, "\n")
            self.sendSocket.sendto(query_plus_data.encode("utf-8"), ("255.255.255.255", self.query_port))

    def queryResultHandler(self, res):
        self.child.query_result_data(res)


if __name__ == '__main__':
    # 初始化全局变量
    glo._init()
    glo.set_value("deviceId", 1001)

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    childWin = ChildWindow()
    # 绑定信号槽
    btn_1001 = mainWin.main_ui.set_button_1001
    btn_1001.clicked.connect(childWin.show)
    btn_1002 = mainWin.main_ui.set_button_1002
    btn_1002.clicked.connect(childWin.show)
    btn_1003 = mainWin.main_ui.set_button_1003
    btn_1003.clicked.connect(childWin.show)

    mainWin.show()
    sys.exit(app.exec_())
