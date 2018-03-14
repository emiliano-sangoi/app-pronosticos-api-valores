# http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/
activate_this = '/var/www/html/cevarcam_api/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, "/var/www/html/cevarcam_api")
from cevarcam_api import app as application
