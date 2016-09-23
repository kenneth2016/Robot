 
class Robot(object):
	def __init__(self,x,y):
		self.direccion="^"
		self.x=x
		self.y=y
		self.fichas=0
		self.mapa= None

	def move(self):
		if self.direccion==">" and self.x<ancho:
			self.x+=1	
		elif self.direccion=="v" and self.y<alto:
			self.y+=1
		elif self.direccion=="<" and self.x>0:
			self.x-=1
		elif self.direccion=="^" and self.y>0:
			self.y-=1				
	
	def rotate(self):
		if self.direccion=="^":
			self.direccion=">"
		elif self.direccion==">":
			self.direccion="v"
		elif self.direccion=="v":
			self.direccion="<"
		elif self.direccion=="<":
			self.direccion="^"						
	
	def asignar_mapa(self, mapa):
		self.mapa = mapa

	def recoger(self):
		if self.mapa.contar_monedas_en(self.x, self.y) > 0:
			self.monedas += 1
			self.mapa.remover_moneda_en(x, y)

	def dibujar(self):
		return self.direccion

