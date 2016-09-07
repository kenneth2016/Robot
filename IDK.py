mapa_completo =[]
def cargar_mapa(mapa):

	f = open(mapa , "r")

	for line in f:
		mapa_completo.append(list (line.strip()))

	return mapa_completo
		
mi_mapa= cargar_mapa("mapas/mapa1.txt")
print (mapa_completo)

ordenes = []
def cargar_instrucciones(instrucciones):
	
	o = open(instrucciones, "r")
	for regla in o:
		ordenes.append(list(regla.split()))
	return ordenes

reglas= cargar_instrucciones("instrucciones/programa1.txt")
print (ordenes)