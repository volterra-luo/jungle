# -*- coding: utf-8 -*-
import hashlib


def sign(text, key, input_charset):
	m = hashlib.md5()
	raw_str = text + key
	tmp_str = unicode(raw_str, input_charset)
	m.update(tmp_str)

	return m.hexdigest()

def verify(text, key, sign, input_charset):
	
	mysign = MD5.sign(text, key, input_charset)

	if mysign == sign:
		return True

	return False
