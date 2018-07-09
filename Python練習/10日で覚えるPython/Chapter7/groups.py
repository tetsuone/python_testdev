class Groups(object):
	def __init__(self):
		self._d = {}

	def contain(self, k, v):
		return v in self._d.get(k,())

	def add(self, k, v):
		self._d.setdefault(k, set()).add(v)

	def remove(self, k, v):
		if k in self._d:
			self._d[k].discard(v)

	def count(self, k):
		return len(self._d.get(k,()))



