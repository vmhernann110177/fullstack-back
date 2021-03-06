"""
Full stack pedir una pizza
"""
from flask import Flask, request, redirect, Response
app = Flask(__name__)

@app.route("/hello")
def hello():
    """
    Hello world, prueba
    """
    return "<html><body><div>Hello world, since flask II!</div></body></html>"

@app.route("/pizza", methods=['POST'])
def pizza():
    """
    pedir una pizza
    """
    parametro_1 = request.form.get("p1")
    parametro_2 = request.form.get("p2")
    #Aqui se imprime en la condsola de python, NOmbre y Apellido.
    print(parametro_1)
    print(parametro_2)
    # Esto no queda claro del todo, lo pongo pero no veo a donde llega,
    # Siento que hace falta una breve explicacion en los videos de la clase.
    # Sin embargo, si corrió muy bien en Postman!
    # Aclaro que en postman hay que hacer click en "Preview"
    #para ver la pagina: solicita_pedido.html
    return redirect("http://localhost/solicita_pedido.html", code=302)

    ### La siguiente linea la puse para ver un html en postman con nombre y apellido, si funciona
    ### pero no se pide en la actividad y por ello, solo lo dejo comentado:
    # return "<html><body><div>Hello "+p1+ " " + p2 +"!</div></body></html>"

    ####--------------####
    # Yo no tengo esto, va despues de la linea=23:
@app.route("/checksize", methods=['POST'])
def checksize():
    """
    comprueba disponibilidad de un tamaño de pizza
    debe capturar el parametro "size"  de la request.
    debe retornar siempre "Disponible"
    Excepto para el tamaño "S" que debe retornar "No disponible"
    """
    size = request.form.get("size")
    if size == "S":
        status = "No disponible"
    else:
        status = "Disponible"
    return Response(status, 200, {'access-Control-Allow-Origin': '#'})
