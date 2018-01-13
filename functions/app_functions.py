from functions.netcdf_functions import *
import json


def getVariablesMeteorologicas():
    variables = get_variables()
    return json.dumps(variables)

def getEstado():
    estado = check_estado()
    return json.dumps(estado)

def getDimensiones():
    dimensiones = get_dimensiones()
    return json.dumps(dimensiones)

def getLatLngs():
    lat_lng = get_lat_long();
    return json.dumps(lat_lng);

def getLimiteRect():
    limites = get_limites_rect()
    return json.dumps(limites)