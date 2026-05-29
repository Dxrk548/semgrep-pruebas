from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)

def cifrar_imagen(input_file, output_file):

    cipher = ChaCha20.new(key=key)

    with open(input_file, 'rb') as f:
        data = f.read()

    ciphertext = cipher.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(cipher.nonce)
        f.write(ciphertext)

    print("Imagen cifrada")


def descifrar_imagen(input_file, output_file):

    with open(input_file, 'rb') as f:
        nonce = f.read(8)
        ciphertext = f.read()

    cipher = ChaCha20.new(key=key, nonce=nonce)

    plaintext = cipher.decrypt(ciphertext)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print("Imagen descifrada")


cifrar_imagen("Col.png", "Lin.tiff")
descifrar_imagen("Lin.tiff", "Col.png")