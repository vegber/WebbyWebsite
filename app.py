from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
import io
import os
import uuid
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from blockcipher.S_BOX import *
from blockcipher.DataManagement import *
from blockcipher import AES
from blockcipher.AES import *
from blockcipher.DataManagement import *
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True


def format_to_hex(key, plaintext):

    return stream_to_blocks(ascii_to_hex(key)), stream_to_blocks(ascii_to_hex(plaintext))


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


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    global img_url
    img_url = url_for('static', filename='AES.jpeg')

    if request.method == 'GET':
        return render_template('index2.html', image_url=img_url)
    elif request.method == 'POST':
        plaintext = request.form.get('Encryption_field')
        key = request.form.get("Key_field")
        dec = request.form.get('Decryption_field')
        # Encrypt
        if dec == '' and plaintext != '':
            evensized = do_encryption(key, plaintext)
        else:
            evensized = do_decryption(key, dec)
        return render_template('encrypted.html', image_url=img_url, data=evensized)
    else:
        return render_template('error404.html')


def do_encryption(key, plaintext):
    ciphertext = encrypt(key, plaintext)
    a = [x for x in ciphertext]
    evensized = [''.join(a[i:i + 32]) for i in range(0, len(a), 32)]
    return evensized


#
def do_the_login():
    pass


def show_the_login_form():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run()
