import os, sys

sys.path.append('/var/www/Joshua-web')
sys.path.append('/var/www/Joshua-web/Joshua')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


#use this for older version of apache
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
