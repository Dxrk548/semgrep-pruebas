from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

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

    print("Imagen cifrada")


def descifrar_imagen(input_file, output_file):

    with open(input_file, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print("Imagen descifrada")


cifrar_imagen("Col.png", "Lin.tiff")
descifrar_imagen("Lin.tiff", "Col.png")