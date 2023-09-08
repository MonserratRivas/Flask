from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('index.html')  
    

@app.route('/play')
def play():
    return render_template('play/4/4')

@app.route('/play/<row>/<col>')
def play(row,col):
    row = int(row)
    col = int(col)
    return render_template('play/index.html',fila=row, columna=row)

if __name__=="__main__":
    app.run(debug=True)