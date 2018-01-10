import functions.temperatura_functions
from index import app

@app.route('/temperatura')
def temperatura_home():
	return "Home de temperatura"