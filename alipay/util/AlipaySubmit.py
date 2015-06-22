# -*- coding: utf-8 -*-

import AlipayCore
from alipay.config import AlipayConfig
from alipay.sign import MD5

# 支付宝提供给商户的服务接入网关URL(新)
ALIPAY_GATEWAY_NEW = 'https://mapi.alipay.com/gateway.do?'


'''
    生成签名结果
    param sPara 要签名的数组({})
    return 签名结果字符串
'''


def buildRequestMysign(sPara):
    # 把字典中所有元素，按照“参数=参数值”的模式用“&”字符拼接并且排序组成字符串
    prestr = AlipayCore.createLinkString(sPara)
    mysign = ''
    if AlipayConfig.sign_type == 'MD5':
        mysign = MD5.sign(prestr, AlipayConfig.key, AlipayConfig.input_charset)

    return mysign

'''
    生成要请求给支付宝的参数数组
    param sParaTemp 请求前的参数数组({})
    return 要请求的参数数组({})
'''


def buildRequestPara(sParaTemp):

    # 除去字典中的空值和签名参数
    sPara = AlipayCore.paraFilter(sParaTemp)

    # 生成签名结果
    mysign = buildRequestMysign(sPara)

    # 签名结果与签名方式加入请求提交参数组中
    sPara['sign'] = mysign
    sPara['sign_type'] = AlipayConfig.sign_type

    return sPara

'''
    建立请求，以表单HTML形式构造（默认）
    param sParaTemp 请求参数数组({})
    param strMethod 提交方式。两个值可选：post、get
    param strButtonName 确认按钮显示文字
    return 提交表单HTML文本
'''


def buildRequest(sParaTemp, strMethod, strButtonName):
    # 待请求参数数组字典
    sPara = buildRequestPara(sParaTemp)
    keys = sPara.keys()

    sbHtml = ''
    tmp_str = r'<form id="alipaysubmit" name="alipaysubmit" action="%s_input_charset=%s\" method="%s">' \
        % (ALIPAY_GATEWAY_NEW, AlipayConfig.input_charset, strMethod)
    sbHtml += tmp_str

    for key in keys:
        value = sPara.get(key)
        tmp_str = r'<input type="hidden" name="%s" value="%s"/>' % (key, value)
        sbHtml += tmp_str

    # submit按钮控件请不要含有name属性
    sbHtml += r'<input type="submit" value="%s" style="display:none;"></form>' % (strButtonName,)
    sbHtml += r'<script>document.forms["alipaysubmit"].submit();</script>'

    return sbHtml

'''
    用于防钓鱼，调用接口query_timestamp来获取时间戳的处理函数
    注意：远程解析XML出错，与服务器是否支持SSL等配置有关
    return 时间戳字符串
'''
def query_timestamp():
    pass

