class KeyPair:
	def __init__(self, name, value):
		self.name = name
		self.value = value
		self.state = 0

	def Name(self):
		return self.name

	def Value(self): 
		return self.value
