import functions.viento_functions
from cevarcam_api import app

@app.route("/viento")
def viento_home():
	return "Home de viento"