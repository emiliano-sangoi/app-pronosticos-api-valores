from functions.app_functions import *
from functions.temperatura_functions import *
from functions.precipitacion_functions import *
from functions.viento_functions import *

from index import app
import json

@app.route("/")
def indexAction():
    rutas = {
        "/variables" : "Devuelve las variables definidas en el archivo.",
        "/dimensiones" : "Devuelve las dimensiones definidas en el archivo.",
        "/estado" : "Devuelve informacion sobre el estado general del servicio web.",
        "/<variable>/valores" : "Devuelve los valores asociados a esa variable. Para ver las variables disponibles ingresar a /variables"
    };
    return json.dumps(rutas)

# Muestra las variables existenes
@app.route("/variables")
def variablesAction():
    return getVariablesMeteorologicas()

@app.route("/dimensiones", methods=['GET'])
def dimensionesAction():
	return getDimensiones()

# @app.route("/dimensiones/<string:dimension>", methods=['GET'])
# def dimensionesAction(dimension):
# 	return getDimensionesInfo(dimension)

@app.route("/estado")
def estadoAction():
	return verificarEstado()

@app.route('/<string:variable>/valores')
def get_valores_action(variable):
    if variable == 'temperatura':
        return temperatura_valores()
    elif variable == 'viento':
        return viento_valores()
    elif variable == 'precipitacion':
        return precipitacion_valores()
	return False