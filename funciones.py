from netCDF4 import Dataset
from pprint import pprint
import json


##########################################################################################
# Docs utiles
# Referencia NetCDF4
#   http://unidata.github.io/netcdf4-python

def getArchivoDatos():
    file = 'wrf_20170823d_full.nc'
    return { 'nombre': file, 'ruta' : "files/" + file }

def openArchivoDatos():
    archivo = getArchivoDatos()

    try:
        fileHandler = Dataset(archivo['ruta'], "r", format="NETCDF4")
        return fileHandler
    except IOError:
        pass

    return False




def hola():
    #rootgrp = Dataset("files/wrf_2017-05-29.nc", "r", format="NETCDF3_CLASSIC")
    rootgrp = Dataset("files/wrf_20170823_full.nc", "r", format="NETCDF4")
    variables = rootgrp.variables
    # dset = Dataset.variables  # Leo variables (diccionario)

    # Muestro nombres de variables y los guardo en una lista:
    lista_nombres = []
    print("\nNombres abreviados de las variables almacenadas en el NetCDF:\n")
    for nombre in variables:
        lista_nombres.append(nombre)
        print(nombre)

    pprint(variables)
    return json.dumps(lista_nombres)

def getVariables():
        # rootgrp = Dataset("files/wrf_2017-05-29.nc", "r", format="NETCDF3_CLASSIC")
        rootgrp = Dataset("files/wrf_20170823_full.nc", "r", format="NETCDF4")
        variables = rootgrp.variables
        # dset = Dataset.variables  # Leo variables (diccionario)

        # Muestro nombres de variables y los guardo en una lista:
        lista_nombres = []
        for nombre in variables:
            lista_nombres.append(nombre)

        return json.dumps(lista_nombres)

# Diccionarios en Python
# https://docs.python.org/2/tutorial/datastructures.html#dictionaries
def checkEstado():

        archivo = getArchivoDatos()
        estado = {'archivo': archivo['ruta'], 'errores' : [], 'estado' : 'OK', 'msg' : "Para poder realizar consultas el estado del servicio debe ser OK." }

        # Abrir archivo:
        fileHandler = openArchivoDatos()

        errores = []
        if fileHandler == False:
            errores.append("Error al intentar abrir el archivo de datos. Probablemente este error se debe a que no se pudo encontrar el archivo u posee algun error.")
        else:
            variables = fileHandler.variables

            # Muestro nombres de variables y los guardo en una lista:
            lista_nombres = []
            for nombre in variables:
                lista_nombres.append(nombre)

            estado['variables'] = lista_nombres

        estado['errores'] = errores

        if len(errores) > 0:
            estado['estado'] = 'NOT_OK'

        return json.dumps(estado)
