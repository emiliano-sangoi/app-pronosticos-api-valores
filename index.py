from flask import Flask
from funciones import hola, getVariables, checkEstado
app = Flask(__name__)

@app.route("/")
def indexAction():
	r = hola()
	return r
	#return "Hello World!!!"

# Muestra las variables existenes
@app.route("/variables")
def variablesAction():
	return getVariables()

@app.route("/estado")
def estadoAction():
	return checkEstado()

@app.route("/temperatura")
def temperatura_home():
	return "Home de temperatura"

@app.route("/precipitacion")
def precipitacion_home():
	return "Home de precipitacion"

@app.route("/viento")
def viento_home():
	return "Home de viento"

if __name__ == '__main__':
	app.run(port=5000,  debug=True)
