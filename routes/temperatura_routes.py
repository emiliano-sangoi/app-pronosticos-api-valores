from functions.temperatura_functions import *
from cevarcam_api import app

@app.route('/temperatura')
def temperatura_home_action():
	return "Home de temperatura"

