this package serve as API and UI for Joshua Arabic to English translation service that are build from Joshua Machine Translation ToolKit.
for more detail, see http://joshua-decoder.org/

this application assume you have your Joshua service installed and you could call Joshua scripts to complete the translation.

change Joshua/setting.py JOSHUA_SCRIPT_EXECUTABLE and JOSHUA_SCRIPT_FILENAME to reflect your Joshua server setup 
see conf/translate_input.sh for sample script that take stdin and netcat to Joshua server


following are python dependences that are required to be installed.
assuming python 2.7+ is installed.

#use pip to install needed component
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
pip install django==1.8
pip install markdown defusedxml
pip install lxml
pip install dateutil
pip install pyyaml
pip install django-tastypie


 
 Depends on version of tastypie you have install, you might also need to copy files in patch folder to 
 $Python/dist-packages/tastype folder:
 
	To support UTF8 encoding of result data from API for json format, modify 
	utils/mime.py to comment out 
	if format in ('application/json', 'text/javascript'):
 		    return format
 	or simply copy patch/tastpie/utils/mime.py to $Python/dist-packages/tastype/utils folder.
 	
 	copy patch/tastpie/resources.py to $Python/dist-packages/tastype/utils if see run time error on resources.py.
 	(tastypie>0.12.1 should have fix the issue).
 	
 	

 to start Django server, enter:
 copy Joshua folder to the server where Joshua script is avaialble. 
   cd Joshua 
  python manage.py runserver 0.0.0.0:80
 
API is available at
http://localhost:80/api/translation/?format=json&orig_text=" " , it also support format=xml
http://localhost:80 will return a user interface to enter text in the text area.


to start up django server automatically in centos, install supervisord in centos and put
conf/supervisord/django_cms.conf to the include folder.
 see https://rayed.com/wordpress/?p=1496 for detail of how to install and setup supervisor.


for more production configuration, you might want to deploying Django with Apache and mod_wsgi

 install mod_wsgi to your Apache server, append your Apache server’s httpd.conf file with conf/apache/httpd.conf file.
 this assume, you are copying Joshua-web folder to /var/www/ folder.
 
 tested configuration in  ubuntu:
	 apt-get install libapache2-mod-wsgi
	 nano /etc/apache2/sites-enabled/000-default
	  
	 and add  following lines just below <VirtualHost *:80>
	
		WSGIDaemonProcess Joshua-web 		
		WSGIProcessGroup Joshua-web
		WSGIScriptAlias / /var/www/Joshua-web/conf/apache/django.wsgi
 		Alias /static /var/www/Joshua-web/static
   		Alias /media   /var/www/Joshua-web/static/

    service apache2 restart
   


