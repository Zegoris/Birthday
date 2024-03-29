from flask import Flask, render_template
from text import text


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Нюта')

@app.route('/text')
def congratulation():
    return render_template('text.html', name='Нюта', text=text.split('\n'))

@app.route('/image')
def image():
    return render_template('img.html', name='Нюта')

if __name__ == '__main__':
    app.run(port=7070, host='0.0.0.0')