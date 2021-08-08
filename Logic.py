from blockcipher.AES import Cipher
from blockcipher.DataManagement import stream_to_blocks, ascii_to_hex, two_by_two_to_str, hex_to_ascii


def do_decryption(key, cipher_text):
    # assume ciphertext is in hex
    hexed_key = stream_to_blocks(ascii_to_hex(key))
    ciphered_ = stream_to_blocks(cipher_text)
    decrypted = ""
    for x in range(len(ciphered_)):
        aes = Cipher(''.join(hexed_key), ''.join(ciphered_[x]), 128)
        aes.Decrypt()
        aes.zerofix()
        decrypted += two_by_two_to_str(aes.state)
    #     a = [x for x in ciphertext]
    a = [x for x in decrypted]
    evensized = [''.join(a[i:i + 32]) for i in range(0, len(a), 32)]
    out = ""
    for x in evensized:
        out += hex_to_ascii(x)
    return ([out])
    # return hex_to_ascii(decrypted)
    # return list(hex_to_ascii(decrypted))


def encrypt(key, plaintext):
    # todo
    hexed_key, hexed_plaintext = format_to_hex(key, plaintext)
    key_frase = ''.join(hexed_key)
    ciphertext = ''
    for x in range(len(hexed_plaintext)):
        aes = Cipher(key_frase, ''.join(hexed_plaintext[x]), 128)
        aes.Encrypt()
        aes.zerofix()
        ciphertext += two_by_two_to_str(aes.state)

    return ciphertext


def format_to_hex(key, plaintext):
    return stream_to_blocks(ascii_to_hex(key)), stream_to_blocks(ascii_to_hex(plaintext))


def do_encryption(key, plaintext):
    ciphertext = encrypt(key, plaintext)
    a = [x for x in ciphertext]
    evensized = [''.join(a[i:i + 32]) for i in range(0, len(a), 32)]
    return evensized