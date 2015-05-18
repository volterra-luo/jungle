# -*- coding: utf-8 -*-

from alipay.config import AlipayConfig

"""
	除去数组中的空值和签名参数
	param sArray 签名参数组
    return 去掉空值与签名参数后的新签名参数组
"""


def paraFilter(sArray):
    result = {}

    if sArray == None or len(sArray) == 0:
        return result

    for key, value in sArray.iteritems():

        if value is None or value == "" or key.lower() == 'sign' or key.lower() == 'sign_type':
            continue

        result[key] = value

    return result

'''
	把数组所有元素排序，并按照“参数=参数值”的模式用“&”字符拼接成字符串
    param params 需要排序并参与字符拼接的参数组
    return 拼接后字符串
'''


def createLinkString(params):
    prestr = ''
    keys = params.keys()
    keys.sort()

    tmp = []
    for key in keys:
        value = params.get(key)
        tmp.extend([key, "=", value, "&"])

    tmp.pop()
    prestr = ''.join(tmp)
    return prestr

'''
	写日志，方便测试(看网站需求，也可以改成把记录存入数据库)
	param sWord 要写入日志里的文本内容
'''


def logResult(sWord):
    pass

'''
	生成文件摘要
    param strFilePath 文件路径
    param file_digest_type 摘要算法
    return 文件摘要结果
'''


def getAbstract(strFilePath, file_digest_type):
    pass
