from flask import Flask
from flask import request
from flask import Flask, request
from flask import Flask, request, redirect
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<html><body><div>Hello world, since flask II!</div></body></html>"

@app.route("/pizza", methods=['POST'])
def pizza():
    p1 = request.form.get("p1")
    p2 = request.form.get("p2")
    #Aqui se imprime en la condsola de python, NOmbre y Apellido.
    print(p1)
    print(p2)
    # Esto no queda claro del todo, lo pongo pero no veo a donde llega, Siento que hace falta una breve explicacion en los videos de la clase.
    # Sin embargo, si corrió muy bien en Postman!
    # Aclaro que en postman hay que hacer click en "Preview" para ver la pagina: solicita_pedido.html
    return redirect("http://localhost/solicita_pedido.html", code=302)
    
    ### La siguiente linea la puse para ver un html en postman con nombre y apellido, si funciona
    ### pero no se pide en la actividad y por ello, solo lo dejo comentado:
    # return "<html><body><div>Hello "+p1+ " " + p2 +"!</div></body></html>"
    