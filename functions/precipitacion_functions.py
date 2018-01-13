from netcdf_functions import *
import json

#------------------------------------------------------------------------------------------------------------------

def precipitacion_valores():
    res = variable_valores('precip')
    return json.dumps(res)