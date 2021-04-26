import serial


def send(data):  # 发送函数
    serial1 = serial.Serial('com1', 9600, timeout=1)
    serial1.write(data)  # 用write函数向串口发送数据



class Connection(object):

    def __init__(self, timeout=1):
        pass

    def receive(self):  # 接收函数
        while True:  # 循环接收数据
            while self.serial1.inWaiting() > 0:  # 当接收缓冲区中的数据不为零时，执行下面的代码
                output = self.serial1.read(7)  # 提取接收缓冲区中的前7个字节数
                print(output.decode('gbk'))
                return output
