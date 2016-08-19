
def cargar_mapa(mapa):
	mapa_completo =[]
	f = open(mapa , "r")

	for line in f:
		mapa_completo.append(list (line.strip()))

	return mapa_completo
		
mi_mapa= cargar_mapa("mapas/mapa1.txt")
print (mapa_completo)
