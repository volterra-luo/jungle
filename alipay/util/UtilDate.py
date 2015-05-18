# -*- coding: utf-8 -*-
from time import time, localtime, strftime
from random import randint


# 年月日时分秒(无下划线) yyyyMMddHHmmss
dtLong = '%Y%m%d%H%M%S'

# 完整时间 yyyy-MM-dd HH:mm:ss
simple = '%Y-%m-%d %H:%M:%S'

# 年月日(无下划线) yyyyMMdd
dtShort = '%Y%m%d'

'''
    返回系统当前时间(精确到毫秒),作为一个唯一的订单编号
    return
        以yyyyMMddHHmmss为格式的当前系统时间
'''


def getOrderNum():
    return strftime(dtLong, localtime(time()))


'''
	获取系统当前日期(精确到毫秒)，格式：yyyy-MM-dd HH:mm:ss
'''


def getDateFormatter():
    return strftime(simple, localtime(time()))

'''
	获取系统当期年月日(精确到天)，格式：yyyyMMdd
'''


def getDate():
    return strftime(dtShort, localtime(time()))

'''
	产生随机的三位数
'''


def getThree():
    num = randint(100, 999)
    return str(num)
