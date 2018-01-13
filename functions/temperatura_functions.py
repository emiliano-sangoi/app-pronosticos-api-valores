from netcdf_functions import *
import json

#------------------------------------------------------------------------------------------------------------------
def temperatura_valores():
    res = variable_valores("temperature")
    return json.dumps(res)