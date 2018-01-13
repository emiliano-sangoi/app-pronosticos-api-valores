from netcdf_functions import *
import json

#------------------------------------------------------------------------------------------------------------------


def viento_valores():
    res = variable_valores('vientov')
    return json.dumps(res)