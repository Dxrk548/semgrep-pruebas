from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

key = get_random_bytes(32)

def cifrar_imagen(input_file, output_file):
    cipher = AES.new(key, AES.MODE_GCM)

    with open(input_file, 'rb') as f:
        data = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(output_file, 'wb') as f:
        f.write(cipher.nonce) 
        f.write(tag)        
        f.write(ciphertext)

    print(f"¡Éxito! Imagen cifrada guardada como: {output_file}")


def descifrar_imagen(input_file, output_file):
    with open(input_file, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        
        with open(output_file, 'wb') as f:
            f.write(plaintext)
        print(f"Imagen descifrada recuperada como: {output_file}")
        
    except ValueError:
        print("Error: La clave es incorrecta o los datos fueron manipulados.")

if os.path.exists("Col.png"):
    cifrar_imagen("Col.png", "imagen_secreta.enc")
    descifrar_imagen("imagen_secreta.enc", "Col_recuperada.png")