from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

@app.route('/')
def index():
    print("Got Post Info")
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # aquí agregamos dos propiedades a la sesión para almacenar el nombre y el correo electrónico
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')