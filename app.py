from flask import Flask, render_template
from flask import request, url_for
from Logic import do_decryption, do_encryption

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = False


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    img_url = url_for('static', filename='AES.jpeg')
    return render_template('index.html', image_url=img_url)


@app.route('/encrypt', methods=['POST'])
def encryption():
    img_url = url_for('static', filename='AES.jpeg')
    if request.method == 'POST':
        plaintext = request.form.get('Encryption_field')
        key = request.form.get('Key_field')
        if plaintext == '':
            return render_template('index.html', image_url=img_url)

        try:
            data = ''.join(do_encryption(key, plaintext))
        except:
            print("Error occurred during encryption! ")
            data = "Ups something went wrong"
        try:
            return render_template('encrypted.html', image_url=img_url, data=data)
        except:
            render_template('error404.html', img_url=img_url)


@app.route('/decrypt', methods=['POST'])
def decryption():
    img_url = url_for('static', filename='AES.jpeg')
    if request.method == 'POST':
        cipher_text = request.form.get('Decryption_field')
        key = request.form.get('Key_field')

        if cipher_text == '':
            return render_template('index.html', image_url=img_url)

        try:
            data = do_decryption(key, cipher_text)
        except:
            print("Error occurred during decryption! ")
            data = "Ups something went wrong"
        try:
            return render_template('decrypted.html', image_url=img_url, data=data)
        except:
            render_template('error404.html', img_url=img_url)


@app.route('/About')
def about():
    img_url = url_for('static', filename='AES.jpeg')
    return render_template('About.html', image_url=img_url)


@app.route('/Home')
def home():
    img_url = url_for('static', filename='AES.jpeg')
    return render_template('index.html', image_url=img_url)


if __name__ == '__main__':
    app.run()
