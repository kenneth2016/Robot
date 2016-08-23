class Robot(object):
	def __init__(self, direccion, x, y, fichas, mapa):
		self.direccion = 0
		self.x = 0
		self.y = 0
		self.fichas = 0
		self.mapa = mapa_completo

	def move(self):
		if self.direccion==0 and self.x < 80:
			self.x +=1

		if self.direccion==90 and self.y < 25:
			self.y +=1

		if self.direccion==180 and self.x < 80:
			self.x -=1

		if self.direccion==270 and self.y < 25:
			self.y -=1

	def rotar(self):
		self.direccion+=90
		if self.direccion>360:
			self.direccion=0

	def recoger(self):
		



