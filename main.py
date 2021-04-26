import sys
import threading

from common import glo
from ui import designer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
import socket
import action.listener
import survive.heartBeat


class MainDlg(QDialog, designer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainDlg, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        # 控制功能选择的节点
        self.node_list = []

        # 创建广播发送器
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.slave_to_master = "0812"
        self.master_to_slave = "0827"
        self.control_type = "0625"
        self.control_port = 8000
        self.run_mode_1 = "2301"
        self.run_mode_2 = "2302"
        self.run_mode_3 = "2303"
        self.fake_vid = "0000000000000000"

    def initUI(self):
        self.textEdit.setText("返回内容:")
        self.search_start.setDisabled(0)

    @pyqtSlot()
    def on_search_start_clicked(self):
        print("点击了搜索从站按钮,开启监听线程...")
        # 实例化组网报文监测
        self.recvThread = action.listener.ReceiveThread()
        # 连接信号槽
        self.recvThread.receive_signal.connect(self.handlerDisplay)
        # 开启线程
        self.recvThread.start()

        # 启动心跳报文监测
        self.heartBeatThread = action.listener.HeartBeatListener()
        self.heartBeatThread.receive_heartbeat_signal.connect(self.heartbeatHandler)
        self.heartBeatThread.start()

    @pyqtSlot()
    def on_motion_control_clicked(self):
        print("点击了运动控制按钮，开启运动控制功能...")
        if 1001 != glo.get_value("deviceId"):
            cur_device_id = glo.get_value("deviceId")
            # 添加当前设备id到combobox选项中
            for i in range(1001, cur_device_id):
                self.node_list.append(str(i))
                self.comboBox.addItem(str(i))
                self.comboBox_2.addItem(str(i))
        else:
            print("未发现活跃的从站设备...")
            QMessageBox.information(self, '信息提示对话框', "未发现活跃的从站设备！")

    @pyqtSlot()
    def on_run_mode_1_clicked(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>启动运动模式1<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        if self.comboBox.currentText() == "":
            print("请先打开控制功能，选择要操作的从站节点！")
            QMessageBox.information(self, '信息提示对话框', "请先打开控制功能，选择要操作的从站节点！")
        else:
            # 获取控制的节点
            node_1 = self.comboBox.currentText()
            node_2 = self.comboBox_2.currentText()
            if node_1 == node_2:
                # 组装消息帧，发送给控制端口
                run_data = self.control_type + "0001" + node_1 + self.run_mode_1 + self.fake_vid
                print("发送的控制指令：", run_data)
                self.sendSocket.sendto(run_data.encode("utf-8"), ("255.255.255.255", self.control_port))
            else:
                # 组装消息帧，发送给控制端口
                run_data_1 = self.control_type + "0001" + node_1 + self.run_mode_1 + self.fake_vid
                self.sendSocket.sendto(run_data_1.encode("utf-8"), ("255.255.255.255", self.control_port))
                run_data_2 = self.control_type + "0001" + node_1 + self.run_mode_1 + self.fake_vid
                self.sendSocket.sendto(run_data_2.encode("utf-8"), ("255.255.255.255", self.control_port))

    @pyqtSlot()
    def on_run_mode_2_clicked(self):
        print("启动运动模式2........")
        # 组装消息帧，发送给控制端口
        run_data_2 = ""
        self.sendSocket.sendto(run_data_2.encode("utf-8"), ("255.255.255.255", self.control_port))

    @pyqtSlot()
    def on_run_mode_2_clicked(self):
        print("启动运动模式2........")
        # 组装消息帧，发送给控制端口
        run_data_3 = ""
        self.sendSocket.sendto(run_data_3.encode("utf-8"), ("255.255.255.255", self.control_port))

    def handlerDisplay(self, msg, ip):
        print("----------------组网信号槽函数触发-----------------")
        if 200 == self.judgeData(msg, ip):
            print("收到从站组网请求，请求正确，成功返回数据, 设备入网成功")
            self.textEdit.append(str(msg))

    def heartbeatHandler(self, msg):
        print("----------------心跳信号槽函数触发-----------------")
        if 200 == self.judgeAliveMsg(msg):
            print("从站心跳信号，请求正确，操作完成")

    def offlineHandler(self, de_id):
        print("----------------设备离线信号槽函数触发-----------------")
        print("进行离线操作...")
        node_status = "offline"
        if de_id == "1001":
            self.lineEdit_105.setText(node_status)
        elif de_id == "1002":
            self.lineEdit_205.setText(node_status)
        elif de_id == "1003":
            self.lineEdit_305.setText(node_status)
        else:
            print("设备id错误，请检查")

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
            # 组装数据帧并返回
            response_data = self.master_to_slave + organization_status + device_id + device_status + device_vid
            print("返回给从站的响应数据为: " + response_data)
            print("设备入网配置完成，设备类型: %s || 设备ID: %s || 设备信息: %s || 设备VID: %s" % (
                device_type, device_id, device_info, device_vid))
            self.sendSocket.sendto(response_data.encode("utf-8"), ("255.255.255.255", 8000))
            # 入网成功、显示在从站列表中，设置line text
            self.showList(device_id, device_type, device_vid, ip, device_status)
            # 保存实例
            print("当前在网实例: ", glo.get_value(device_id))
            glo.set_value(device_id, True)

            # 启动心跳线程，创建一个timer
            self.heartbeatTimerThread = survive.heartBeat.HeartBeatThread()
            # 连接槽函数
            self.heartbeatTimerThread.offline_signal.connect(self.offlineHandler)
            self.heartbeatTimerThread.start()
            # 设备入网id自增
            glo.set_value("deviceId", num + 1)
            return 200

        else:
            print("错误的数据格式，请检查...")
            return 300

    def judgeAliveMsg(self, data):
        alive_status = ""
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

    def showList(self, id, type, vid, ip, status):
        print(id, type, vid, ip, status)
        if id == "1001":
            self.lineEdit_101.setText(id)
            self.lineEdit_102.setText(type)
            self.lineEdit_103.setText(vid)
            self.lineEdit_104.setText(ip)
            self.lineEdit_105.setText(status)
        elif id == "1002":
            self.lineEdit_201.setText(id)
            self.lineEdit_202.setText(type)
            self.lineEdit_203.setText(vid)
            self.lineEdit_204.setText(ip)
            self.lineEdit_205.setText(status)
        elif id == "1003":
            self.lineEdit_301.setText(id)
            self.lineEdit_302.setText(type)
            self.lineEdit_303.setText(vid)
            self.lineEdit_304.setText(ip)
            self.lineEdit_305.setText(status)


if __name__ == '__main__':
    glo._init()
    glo.set_value("deviceId", 1001)
    app = QApplication(sys.argv)
    mainDlg = MainDlg()
    mainDlg.show()
    sys.exit(app.exec_())
