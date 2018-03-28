from functions.app_functions import *
from functions.temperatura_functions import *
from functions.precipitacion_functions import *
from functions.viento_functions import *
from flask import request, jsonify
import sys

from cevarcam_api import app
import json

@app.route("/")
def indexAction():
    rutas = {
        "/variables" : "Devuelve las variables definidas en el archivo.",
        "/dimensiones" : "Devuelve las dimensiones definidas en el archivo.",
        "/estado" : "Devuelve informacion sobre el estado general del servicio web.",
        "/variable/serie?latitud=<lat>&longitud=<lng>" : "Devuelve los valores asociados a esa variable para los dias pronositicados. Para ver las variables disponibles ingresar a /variables",
        "/coords" : "Devuelve las latitudes y longitudes existentes.",
        "/limites" : "Esquina inf. izq. y sup. der. correspondientes a los limites para los valores disponibles. Estas coordenadas pueden ser utilizadas para posicionar correctamente una imagen sobre un mapa.",
        "python-version": sys.version
    };
    return jsonify(rutas),200



# Muestra las variables existenes
@app.route("/variables")
def variablesAction():
    return getVariablesMeteorologicas()



@app.route("/dimensiones", methods=['GET'])
def dimensionesAction():
	return getDimensiones()



@app.route("/coords", methods=['GET'])
def latLngAction():
    return getLatLngs();



@app.route("/estado")
def estadoAction():
	return getEstado()



@app.route("/limites")
def limiteRectAction():
    return getLimiteRect()



@app.route('/<string:variable>/serie')
def get_valores_action(variable):

    latitud = request.args.get("latitud");
    longitud = request.args.get("longitud");

    msgError = ''

    if variable == 'temperature':
         data, res = get_serie_temperatura(latitud, longitud)
         if res:
             return jsonify(data), 200
         msgError = res
    elif variable == 'precip':
        data, res = get_serie_precipitacion(latitud, longitud)
        if res:
            return jsonify(data), 200
        msgError = res
    elif variable == 'vientov':
        data, res = get_serie_vientov(latitud, longitud)
        if res:
            return jsonify(data), 200
        msgError = res
    elif variable == 'vientou':
        data, res = get_serie_vientou(latitud, longitud)
        if res:
            return jsonify(data), 200
        msgError = res

    # return jsonify(get_error_response("La variable: " + string(variable) + " no existe.")), 500
    return jsonify(get_error_response(msgError)), 500
    #
    # elif variable == 'viento':
     #    return viento_valores()
    # elif variable == 'precipitacion':
     #    return precipitacion_valores()
	# return