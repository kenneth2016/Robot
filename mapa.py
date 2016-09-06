class Mapa(object):
	def __init__ (self, ancho, altura):
		self.ancho=ancho
		self.altura=altura
		self.robot=None
		sel.monedas=[]

	def crear_robot(self):
		self.robot = robot



	def agregar_monedas(self, moneda):
		self.monedas.append(moneda)



	def contar_monedas_en(self, x, y):
        contador = 0

        for moneda in self.monedas:
            if moneda.x == x and moneda.y == y:
                contador += 1

        return contador

    def dibujar_mapa(self):
    	 resultado = ""

        for y in range(self.altura):
            for x in range(self.ancho):
                if x == self.robot.x and y == self.robot.y:
                    resultado += self.robot.rotar()

                elif self.contar_monedas_en(x, y) > 0:
                    resultado += self.contar_monedas_en(x, y)
                else:
                    resultado += " "

            resultado += "\n"

        return resultado

    def quitar_moneda(self, x, y):
    	indice_coincidencia = -1
        for indice in range(len(self.monedas)):
            moneda = self.monedas[indice]
            if moneda.x == x and moneda.y == y:
                indice_coincidencia = indice
                break

        if indice_coincidencia >= 0:
            self.monedas.pop(indice_coincidencia)



