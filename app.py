from flask import Flask, render_template
from flask import request, url_for

from Logic import do_decryption, do_encryption

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
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


#
def do_the_login():
    pass


def show_the_login_form():
    pass


@app.route('/About')
def about():
    img_url = url_for('static', filename='AES.jpeg')
    return render_template('About.html', image_url=img_url)


@app.route('/Home')
def home():
    img_url = url_for('static', filename='AES.jpeg')
    return render_template('index2.html', image_url=img_url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


if __name__ == '__main__':
    app.run()
