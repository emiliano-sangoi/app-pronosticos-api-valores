from functions.temperatura_functions import *
from index import app

@app.route('/temperatura')
def temperatura_home_action():
	return "Home de temperatura"
