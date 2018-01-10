import functions.viento_functions
from index import app

@app.route("/viento")
def viento_home():
	return "Home de viento"