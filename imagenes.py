from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

clave = b'12345678'

def cifrar_imagen(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'rb') as f:
        datos = f.read()

    cipher = DES.new(clave, DES.MODE_ECB)
    datos_padded = pad(datos, DES.block_size)
    datos_cifrados = cipher.encrypt(datos_padded)
    with open(archivo_salida, 'wb') as f:
        f.write(datos_cifrados)

    print(f"Imagen cifrada: {archivo_salida}")

def descifrar_imagen(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'rb') as f:
        datos_cifrados = f.read()
    cipher = DES.new(clave, DES.MODE_ECB)
    datos_descifrados = cipher.decrypt(datos_cifrados)
    datos_originales = unpad(datos_descifrados, DES.block_size)
    with open(archivo_salida, 'wb') as f:
        f.write(datos_originales)

    print(f"Imagen descifrada: {archivo_salida}")


cifrar_imagen(
    'wallpaper.tif',
    'imagen_cifrada.des'
)

cifrar_imagen(
    'rdr2.png',
    'imagen_png_cifrada.des'
)

descifrar_imagen(
    'imagen_tif_cifrada.des',
    'imagen_recuperada.tif'
)

descifrar_imagen(
    'imagen_png_cifrada.des',
    'imagen_png_recuperada.png'
)