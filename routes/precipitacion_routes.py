import functions.precipitacion_functions
from index import app

@app.route("/precipitacion")
def precipitacion_home():
	return "Home de precipitacion"

# @app.route('/precipitacion/valores')
# def temperatura_valores_action():
# 	return temperatura_valores()