import sys

def create():
    """Crear archivo.txt"""
    archivo = open('archivo.txt','w')
    archivo.close()

def write():
    """Poner linea en archivo.txt"""
    archivo = open('archivo.txt','a')
    archivo.write('Ejemplo\n')
    archivo.close()


create()
write()
