from django.conf.urls import patterns, include
from Joshua.api import TranslationResource
from Joshua.view import home
#from django.contrib.auth.decorators import login_required

translation_resource = TranslationResource()

urlpatterns = patterns('',
    # The normal jazz here...
    
    (r'^api/', include(translation_resource.urls)),
  
    (r'^$', home), 
     
  
)