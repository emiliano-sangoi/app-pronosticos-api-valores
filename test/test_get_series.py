import json
from pprint import pprint

from functions import *
from functions.netcdf_functions import get_series
from routes.app_routes import get_valores_action

lat = -31.6265705;
longitud = -60.7324942;


res = get_series(lat, longitud);


pprint(res)
