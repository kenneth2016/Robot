 
class Robot(object):
	def __init__(self, direccion, x, y, fichas, mapa):
		self.direccion = "^"
		self.x = x
		self.y = y
		self.fichas = 0
		self.mapa = None

	def colocar_en_mapa(self, mapa):
		self.mapa=mapa

	def move(self):
		if self.direccion==">":
			self.x +=1

		if self.direccion=="v":
			self.y +=1

		if self.direccion=="<":
			self.x -=1

		if self.direccion=="^":
			self.y -=1

	def rotate(self):
		if self.direccion=="^":
			self.direccion=">"

		if self.direccion==">":
			self.direccion="v"

		if self.direccion=="v":
			self.direccion="<"

		else:
			self.direccion = "^"


	def pick(self):
		if self.x == x and self.y == y:
			









