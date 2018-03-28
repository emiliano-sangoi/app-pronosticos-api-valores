from netcdf_functions import *
import json

#------------------------------------------------------------------------------------------------------------------


def viento_valores():
    res = variable_valores('vientov')
    return json.dumps(res)

def get_serie_vientov(la, lo):
    msgError = ''
    try:
        latitud = float(la)
        longitud = float(lo)
        res = get_serie("vientov", latitud, longitud);

        return res, True;
    except ValueError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except TypeError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except:
        msgError = 'Ocurrio un error al procesar la solicitud.'


    if msgError:
        return msgError, False

def get_serie_vientou(la, lo):
    msgError = ''
    try:
        latitud = float(la)
        longitud = float(lo)
        res = get_serie("vientou", latitud, longitud);

        return res, True;
    except ValueError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except TypeError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except:
        msgError = 'Ocurrio un error al procesar la solicitud.'


    if msgError:
        return msgError, False