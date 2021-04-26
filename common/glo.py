# -*- coding: utf-8 -*-
# 主要保存两个数据：当前设备id和设备标志位
# eg. {"deviceId": 1001, "1001" : False, "1002" : True}

def _init():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key, defValue=400):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue
