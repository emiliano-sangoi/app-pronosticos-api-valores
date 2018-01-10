# Funciones para la manipulacion del archivo netcdf

from netCDF4 import Dataset
import json


#------------------------------------------------------------------------------------------------------------------
# Verifica ciertas condiciones necesarias para el correcto funcionamiento del servicio web.
#
# Diccionarios en Python
# https://docs.python.org/2/tutorial/datastructures.html#dictionaries
def checkEstado(asJson=True):
    archivo = getArchivoDatos()
    estado = {'archivo': archivo['ruta'], 'errores': [], 'estado': 'OK',
              'msg': "Para poder realizar consultas el estado del servicio debe ser OK."}

    # Abrir archivo:
    fileHandler = openArchivoDatos()

    errores = []
    if fileHandler == False:
        errores.append(
            "Error al intentar abrir el archivo de datos. Este error se debe a que no se pudo encontrar el archivo u el mismo posee algun error.")
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

    if asJson == True:
        return json.dumps(estado)
    else:
        return estado


# ------------------------------------------------------------------------------------------------------------------
# Devuelve informacion del archivo utilizado
def getArchivoDatos():
    file = 'wrf_20170s823_full.nc'
    return {'nombre': file, 'ruta': "files/" + file}


# ------------------------------------------------------------------------------------------------------------------
# Permite abrir un archivo de datos
def openArchivoDatos():
    archivo = getArchivoDatos()
    try:
        fileHandler = Dataset(archivo['ruta'], "r", format="NETCDF4")
        return fileHandler
    except IOError:
        pass

    return False


# ------------------------------------------------------------------------------------------------------------------
# Muestra las variables meteorologicas definidas en el archivo.
def getVariables():
    fileHandler = openArchivoDatos()

    if fileHandler == False:
        estado = checkEstado(False)
        return json.dumps({'variables': [], 'estado': estado})

    # Muestro nombres de variables y los guardo en una lista:
    lista_nombres = []
    for nombre in fileHandler.variables:
        lista_nombres.append(nombre)

    return json.dumps(lista_nombres)
