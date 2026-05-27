from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def verificar_credenciales():
    datos = request.get_json()
    usuario_ingresado = datos.get('usuario')
    contrasena_ingresada = datos.get('contrasena')
    
    USUARIO_CORRECTO = "Mikolas"
    CONTRASENA_CORRECTA = "upn1234"
    
    if usuario_ingresado == USUARIO_CORRECTO and contrasena_ingresada == CONTRASENA_CORRECTA:
        return jsonify({"valido": True, "mensaje": "¡Ingreso correcto! Cargando interfaz..."})
    else:
        return jsonify({"valido": False, "mensaje": "Usuario o contraseña incorrectos. Inténtalo de nuevo."})

if __name__ == '__main__':
    app.run(debug=True)
