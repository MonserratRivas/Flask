from flask import Flask , render_template , redirect

app = Flask(__name__)

@app.route('/play')
def player():
    return redirect('play/4/4')

@app.route('/play/<row>/<col>')
def play(row,col):
    row = int(row)
    col = int(col)
    return render_template('play/index.html',fila=row, columna=col)

if __name__=="__main__":
    app.run(debug=True)