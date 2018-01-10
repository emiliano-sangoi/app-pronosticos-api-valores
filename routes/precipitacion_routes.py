import functions.precipitacion_functions
from index import app

@app.route("/precipitacion")
def precipitacion_home():
	return "Home de precipitacion"