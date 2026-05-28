from Crypto.Cipher import DES
from Crypto.Util import Counter


clave = b'12345678'


def cifrar_imagen(ruta_entrada, ruta_salida):

  
    with open(ruta_entrada, 'rb') as archivo:
        datos = archivo.read()
    ctr = Counter.new(64)

    cipher = DES.new(clave, DES.MODE_CTR, counter=ctr)

    datos_cifrados = cipher.encrypt(datos)

    with open(ruta_salida, 'wb') as archivo:
        archivo.write(datos_cifrados)

    print("Imagen cifrada:", ruta_salida)

def descifrar_imagen(ruta_entrada, ruta_salida):

    # Leer archivo cifrado
    with open(ruta_entrada, 'rb') as archivo:
        datos_cifrados = archivo.read()

    ctr = Counter.new(64)

    cipher = DES.new(clave, DES.MODE_CTR, counter=ctr)

    datos_descifrados = cipher.decrypt(datos_cifrados)

    with open(ruta_salida, 'wb') as archivo:
        archivo.write(datos_descifrados)

    print("Imagen recuperada:", ruta_salida)


cifrar_imagen("Lin.tiff", "imagen_cifrada.tiff")
cifrar_imagen("Col.png", "imagen_cifrada.png")

descifrar_imagen("imagen_cifrada.tiff", "imagen_recuperada.tiff")
descifrar_imagen("imagen_cifrada.png", "imagen_recuperada.png")