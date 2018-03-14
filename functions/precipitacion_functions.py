from netcdf_functions import *
import json

#------------------------------------------------------------------------------------------------------------------

def precipitacion_valores():
    res = variable_valores('precip')
    return json.dumps(res)


def get_serie_precipitacion(la, lo):

    msgError = ''
    try:
        latitud = float(la)
        longitud = float(lo)
        res = get_serie("precip", latitud, longitud);

        return res, True;
    except ValueError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except TypeError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except:
        msgError = 'Ocurrio un error al procesar la solicitud.'


    if msgError:
        return msgError, False