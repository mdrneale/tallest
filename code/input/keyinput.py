from keypair import KeyPair

class KeyInput:
	def __init__(self, keys):
		self.keys = keys

	def Update(self):
		for key in self.keys:
			