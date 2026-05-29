from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes
import os

key = get_random_bytes(32)


def cifrar_imagen(input_file, output_file):
    cipher = Salsa20.new(key=key)

    with open(input_file, "rb") as f:
        data = f.read()

    ciphertext = cipher.encrypt(data)

    with open(output_file, "wb") as f:
        f.write(cipher.nonce)
        f.write(ciphertext)

    print("Imagen cifrada")


def descifrar_imagen(input_file, output_file):
    with open(input_file, "rb") as f:
        nonce = f.read(8)
        ciphertext = f.read()

    cipher = Salsa20.new(key=key, nonce=nonce)

    plaintext = cipher.decrypt(ciphertext)

    with open(output_file, "wb") as f:
        f.write(plaintext)

    print("Imagen descifrada")


if os.path.exists("Col.png"):
    cifrar_imagen("Col.png", "imagen_salsa.enc")
    descifrar_imagen("imagen_salsa.enc", "Col_salsa_recuperada.png")