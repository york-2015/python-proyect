def lista_principal():
	texto_abierto = open("holadatos.txt")#abre el texto
	lista_de_texto_avierto = [] # esta es la lista principal
	lista_super = [] #mini listas momentanias
	listagrandota = [] #lista prinsipal
	for i in texto_abierto: 
		i = i.strip() #detripalo  
		lista_de_texto_avierto.append(i) #nueva lista sin espasios  
	texto_abierto.close() # serramos el archivo de texto
	for z in lista_de_texto_avierto: #por cada iten de esta lista repite
		if z != "False": 
			lista_super.append(z) #agrega todos menos false
		elif z == "False": #si ese iten es falce 
			lista_copiada = lista_super[:] #esto es un slicing hace una copia para que no sea modificada :)
			listagrandota.append(lista_copiada) # agregar esas lista antes de ser borradas
		 	lista_super.remove(lista_super[0]) #borrala para volverla a usar 
		 	lista_super.remove(lista_super[0]) #cantidad de datos 
	return listagrandota #devuelve el la lista principal

def buscador_de_datos(lista_full):
	palabra_buscada = raw_input("Cual es el nombre: ")
	catidad_de_datos = 2
	for numero_listas in range(len(lista_full)):
		for unidades in range(catidad_de_datos):
			if lista_full[numero_listas][unidades] == palabra_buscada:
				print "esta es la palabra que estas buscando"
				print lista_full[numero_listas]
				for l in lista_full[numero_listas]: #esto las pone mas lindas visiblemente 
					print l

def borar_dato(lista_full):
	palabra_buscada = raw_input("Cual es el nombre: ")
	catidad_de_datos = 2
	for numero_listas in range(len(lista_full)):
		for unidades in range(catidad_de_datos):
			if lista_full[numero_listas][unidades] == palabra_buscada:
				lista_full.remove(lista_full[numero_listas])
				print ("El dato ha sido borrado...")
