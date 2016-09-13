 
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

		elif self.direccion=="v":
			self.y +=1

		elif self.direccion=="<":
			self.x -=1

		elif self.direccion=="^":
			self.y -=1




	def rotate(self):
		if self.direccion=="^":
			self.direccion=">"

		elif self.direccion==">":
			self.direccion="v"

		elif self.direccion=="v":
			self.direccion="<"

		else:
			self.direccion = "^"



	def asingar_mapa(self, mapa):
		self.mapa= mapa

	def recoger(self):
		if self.mapa.contar_monedas_en(self.x, self.y) > 0:
			self.monedas += 1
			self.mapa.quitar_moneda(x, y)

	def dibujar(self):
		return self.direccion
			








