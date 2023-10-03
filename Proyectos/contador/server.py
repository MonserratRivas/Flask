from flask import Flask, render_template, request, make_reponse

app= Flask(__name__)

def obtener_contador():
    contador = request.cookies.get('contador')
    if contador is None:
        return 0
    else:
        return int(contador)

def incrementar_contador(respuesta):
    contador = obtener_contador() + 1
    respuesta.set_cookie('contador', str(contador))
    return respuesta

@app.route('/')
def inicio():
    contador = obtener_contador()
    respuesta = make_response(render_template ('index.html', contador=contador))
    return incrementar_contador(respuesta)


@app.errorhandler(404)
def no_encontrado(error):
    return render_template('404.html'), 404

if __name__== '__main__':
    app.run(debug=True)