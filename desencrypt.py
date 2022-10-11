#!/usr/bin/python3

#encontrar archivos en el directorio actual

archivos = []

for archivo in os.listdir():
	if archivo == "ransoMEL.py" or archivo == "desencrypt.py":
		continue
	if os.path isfile(archivo)
		archivos.append(archivo)
	
print(archivos)

#bucle para desencriptar archivos

for archivo in archivos :
	with open(archivo, "rb") as elarchivo:
		contenidos == elarchivo.read()
	contenidos_desencriptados = Fernet.dencrypt(contenidos)
	with open(archivo, "wb") as elarchivo:
		elarchivo.write(contenidos_desencriptados)
    
    
