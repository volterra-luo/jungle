# -*- coding: utf-8 -*-
import hashlib

#
# 签名字符串
# @param text 需要签名的字符串
# @param key 密钥
# @param input_charset 编码格式
# @return 签名结果
#
def sign(text, key, input_charset):
	m = hashlib.md5()
	raw_str = text + key
	tmp_str = unicode(raw_str, input_charset)
	m.update(tmp_str)

	return m.hexdigest()


#
# 验证签名字符串
# @param text 需要签名的字符串
# @param sign 签名结果
# @param key 密钥
# @param input_charset 编码格式
# @return 验证签名结果
#
def verify(text, key, sign, input_charset):
	
	mysign = MD5.sign(text, key, input_charset)

	if mysign == sign:
		return True

	return False
