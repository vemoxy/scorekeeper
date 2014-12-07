import json

def union(l1, l2):
	return l1 + [i for i in l2 if i not in l1]

def get_extra(obj):
	return json.loads(obj.extra_data)