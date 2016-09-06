 
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

		if self.x < 0:
            self.x = 0

        if self.x >= self.mapa.ancho:
            self.x = self.mapa.ancho - 1

        if self.y < 0:
            self.y = 0

        if self.y >= self.mapa.altura:
            self.y = self.mapa.altura - 1



	def rotate(self):
		if self.direccion=="^":
			self.direccion=">"

		if self.direccion==">":
			self.direccion="v"

		if self.direccion=="v":
			self.direccion="<"

		else:
			self.direccion = "^"



	def asingar_mapa(self, mapa):
        self.mapa = mapa

    def recoger(self):
        if self.mapa.contar_monedas_en(self.x, self.y) > 0:
            self.monedas += 1
            self.mapa.quitar_moneda(x, y)
			








