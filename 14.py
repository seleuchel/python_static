class Tool:
	def __init__(self,name, weight):
		self.name = name
		self.weight = weight

	def __repr__(self):
		return f'Tool ({self.name!r},{self.weight})'

tools = [
	Tool('a', 3.5),
	Tool('b', 1.25),
	Tool('c', 0.5),
	Tool('d', 0.24)
]


tools.sort(key=lambda x: x.name)

