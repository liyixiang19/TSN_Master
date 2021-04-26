import time
from PyQt5 import QtCore
from PyQt5.QtCore import *
from common import glo


class HeartBeatThread(QtCore.QThread):
    offline_signal = pyqtSignal(str)

    def __init__(self):
        super(HeartBeatThread, self).__init__()

        self.device_id_1 = str(glo.get_value("deviceId"))
        print(self.device_id_1)

    def run(self):
        time.sleep(0.5)
        print("\n---------------------------心跳timer开启------------------------")
        counter = 0
        # is_alive = False
        while True:
            time.sleep(1)
            counter = counter + 1
            print("标志位: ", self.device_id_1, "-----", glo.get_value(self.device_id_1))
            print("心跳计时器，设备id：%s, counting down: %s" % (self.device_id_1, str(counter)))
            # 判断当前维护的device的标志位
            if glo.get_value(self.device_id_1) != 400:
                if glo.get_value(self.device_id_1):
                    print("-------------收到心跳，重置计时器------------")
                    # 重置计数器
                    counter = 0
                    # 复位标志位
                    glo.set_value(self.device_id_1, False)
                elif counter > 30:
                    # 超过30s未收到alive信息，设备离线
                    print("设备故障，offline...")
                    if self.device_id_1 == "":
                        print("未知设备")
                    else:
                        print(self.device_id_1 + " 离线")
                        self.offline_signal.emit(self.device_id_1)
                    break
