from robot import Robot
from moneda import Moneda
from mapa import Mapa
import time

mapa_completo= []
def cargar_mapa(mapa):

	f = open(mapa , "r")

	for line in f:
		mapa_completo.append(list (line.strip()))

	return mapa_completo
		
mi_mapa= cargar_mapa("mapas/mapa1.txt")

for y in range(len(mi_mapa)):
	fila = lista[y]
	for x in range(len(mi_mapa)):
		casilla= lista[x][y]
		if casilla == "*":
			robot.colocar_en_mapa

		if casilla== "0":
			pass

		if casilla > 0:
			moneda=self.moneda


def cargar_instrucciones(instrucciones):
	
	o = open(instrucciones, "r")
	for regla in o:
		ordenes.append(list(regla.split()))
	return ordenes
reglas= cargar_instrucciones("instrucciones/programa1.txt")


for i in reglas:

	if i == move:
		robot.move

	if i == rotate:
		robot.rotate

	if i == pick:
		robot.recoger

