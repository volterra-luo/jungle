# -*- coding: utf-8 -*-
import AlipayCore
from config import AlipayConfig

# 支付宝消息验证地址
HTTPS_VERIFY_URL = 'https://mapi.alipay.com/gateway.do?service=notify_verify&'

'''
	验证消息是否是支付宝发出的合法消息
	param params 通知返回来的参数数组({})
    return 验证结果
'''

def verify(params):

	# 判断responsetTxt是否为true，isSign是否为true
	# responsetTxt的结果不是true，与服务器设置问题、合作身份者ID、notify_id一分钟失效有关
	# isSign不是true，与安全校验码、请求时的参数格式（如：带自定义参数等）、编码格式有关
	responseTxt = 'true'

	if params.get('notify_id') != None:
		notify_id = params.get('notify_id')
		responseTxt = verifyResponse(notify_id)

	sign = ''
	if params.get('sign') != None:
		sign = params.get('sign')
		isSign = getSignVeryfy(params, sign)

	# 写日志记录（若要调试，请取消下面两行注释）
	# sWord = u'responseTxt=%s\nisSign=%s\n返回回来的参数：%s' % (responseTxt, isSign, AlipayCore.createLinkString(params))
	# AlipayCore.logResult(sWord)

	if isSign and responseTxt == 'true':
		return True

	return False


'''
	根据反馈回来的信息，生成签名结果
	param Params 通知返回来的参数数组({})
	param sign 比对的签名结果
	return 生成的签名结果
'''

def getSignVeryfy(Params, sign):

	# 过滤空值、sign与sign_type参数
	sParaNew = AlipayCore.paraFilter(Params)

	# 获取待签名字符串
	preSignStr = AlipayCore.createLinkString(sParaNew)

	# 获得签名验证结果
	isSign = False

	if AlipayConfig.sign_type == 'MD5':
		isSign = MD5.verify(preSignStr, sign, AlipayConfig.key, AlipayConfig.input_charset)

	return isSign

'''
	获取远程服务器ATN结果,验证返回URL
	param notify_id 通知校验ID
    return 服务器ATN结果
    验证结果集：
    	invalid命令参数不对 出现这个错误，请检测返回处理中partner和key是否为空 
    	true 返回正确信息
    	false 请检查防火墙或者是服务器阻止端口问题以及验证时间是否超过一分钟
'''

def verifyResponse(notify_id):
	
	# 获取远程服务器ATN结果，验证是否是支付宝服务器发来的请求
	partner = AlipayConfig.partner
	veryfy_url = HTTPS_VERIFY_URL + "partner=" + partner + "&notify_id=" + notify_id

	return checkUrl(veryfy_url)


'''
	获取远程服务器ATN结果
	param urlvalue 指定URL路径地址
	return 服务器ATN结果
    验证结果集：
    	invalid命令参数不对 出现这个错误，请检测返回处理中partner和key是否为空 
    	true 返回正确信息
    	false 请检查防火墙或者是服务器阻止端口问题以及验证时间是否超过一分钟
'''


def checkUrl(urlvalue):
	inputLine = ''

	return inputLine