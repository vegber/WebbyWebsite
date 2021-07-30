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
from blockcipher.DataManagement import ascii_to_hex, two_by_two_to_str
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():



    global img_url
    img_url = url_for('static', filename='AES.jpeg')

    if request.method == 'GET':
        return render_template('index.html', image_url=img_url)
    elif request.method == 'POST':
        print("post")
        plaintext = request.form.get('Encryption_field')
        key = request.form.get("enctext")
        print(key)
        print(ascii_to_hex(key))

        dec = request.form.get('Decryption_field')
        ciphertext = encrypt(key, plaintext)
        return render_template('encrypted.html', image_url=img_url, data=ciphertext)

    else:
        return render_template('error404.html')

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
