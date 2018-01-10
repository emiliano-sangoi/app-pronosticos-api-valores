from functions.app_functions import *
from index import app

@app.route("/")
def indexAction():
	return "Hello World!!!"

# Muestra las variables existenes
@app.route("/variables")
def variablesAction():
    return getVariablesMeteorologicas()

@app.route("/estado")
def estadoAction():
	return checkEstado()