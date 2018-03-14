##########################################################################################
# Servicio Web para consulta de Datos Meteorologicos generados por el modelo WRF y creado
# por personal del Cevarcam (FICH, UNL)
#
# El servicio web es del tipo REST JSON y es fundamental que el archivo de datos se haya
# copiado correctamente
#
# Autor: Emiliano Sangoi
#
# Docs utiles
# Referencia NetCDF4
#   http://unidata.github.io/netcdf4-python
#   http://flask.pocoo.org/docs/0.12/
##########################################################################################


from flask import Flask

app = Flask(__name__)

from routes.app_routes import *
from routes.temperatura_routes import *
from routes.precipitacion_routes import *
from routes.viento_routes import *

if __name__ == '__main__':
	app.run(port=5000,  debug=True, host='127.0.0.1')
