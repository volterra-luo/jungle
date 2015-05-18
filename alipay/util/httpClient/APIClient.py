#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def _parse_json(s):
	'parse str into JsonDict'

	def _obj_hook(pairs):
		' convert json object to python object '
		o = JsonDict()
		for k, v in pairs.iteritems():
			o[str(k)] = v
		return o

	return json.loads(s, encoding='utf-8', object_hook=_obj_hook)

class JsonDict(dict):
    ' general json object that allows attributes to be bound to and also behaves like a dict '

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value

if __name__ == '__main__':
	with open('resp.json','rb') as f:
		print f.name
		s = f.read()
		print isinstance(s, unicode)
		d = _parse_json(s)
		print d.tags[0]['count']