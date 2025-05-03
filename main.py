from flask import Flask,request,render_template



app=Flask(__name__)


@app.route("/")
def home():
    return "PAGINA DE INICIO"

#RUTA PARAMETROS POR URL
@app.route("/consulta")
def ruta_consulta():
    producto=request.args.get("product")
    talla=request.args.get("talla")
    if producto and talla is None:
        return f"Se esta consultando solo el producto {producto}"
    if talla and producto is None:
        return f"Por favor ingrese el producto a consultar"
    if talla is None and producto is None:
        return f"BIENVENIDO A LA PAGINA DE ROPA"

    return f"Se esta consultando el produto {producto} y la talla {talla}"

#RUTA PARA CAPTURAR DATOS POR EL "BODY" 

@app.route("/registro",methods=["GET"])
def registro():
    return render_template("formulario.html")

@app.route("/registro", methods=["POST"])
def procesar_registro():

    nombre=request.form.get("nombre")
    correo=request.form.get("correo")

    return f"El estudiantes a registrar es {nombre} y el correo a registrar es {correo}"

if __name__== "__main__":
    app.run(debug=True)