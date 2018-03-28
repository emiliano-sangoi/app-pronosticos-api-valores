from netcdf_functions import *
from functions.global_functions import *


#------------------------------------------------------------------------------------------------------------------
def get_serie_temperatura(la, lo):
    msgError = ''
    try:
        latitud = float(la)
        longitud = float(lo)
        res = get_serie("temperature", latitud, longitud);

        return res, True;
    except ValueError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except TypeError:
        msgError = 'Los valores de latitud y longitud deben ser numeros decimales. Ambos valores son requeridos.'
    except:
        msgError = 'Ocurrio un error al procesar la solicitud.'


    if msgError:
        return msgError, False