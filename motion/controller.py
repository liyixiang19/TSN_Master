import threading
import time
import motion.serial


class Controller(object):
    def __init__(self):
        self.conn = motion.serial

    def forward(self):
        hex_data = bytes([0x0106, 0x0000, 0x0001, 0x480A])
        self.conn.send(hex_data)

    def back(self):
        hex_data = bytes([0x0106, 0x0001, 0x0001, 0x19CA])
        self.conn.send(hex_data)

    def stop(self):
        hex_data = bytes([0x0106, 0x0002, 0x0001, 0xE9CA])
        self.conn.send(hex_data)

    def queryPlus(self):
        hex_data = bytes([0x0103, 0x0007, 0x0001, 0x35CB])
        self.conn.send(hex_data)


if __name__ == '__main__':
    controller = Controller()
    controller.forward()
