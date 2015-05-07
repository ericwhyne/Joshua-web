from tastypie import fields
from tastypie.bundle import Bundle

import subprocess
from Joshua.cors import CORSModelResource
from Joshua.settings import JOSHUA_SCRIPT_EXECUTABLE
from Joshua.settings import JOSHUA_SCRIPT_FILENAME


class TranslationResource(CORSModelResource):

    orig_text = fields.CharField()
    #orig_language = fields.CharField()(readonly=True, help_text='original text languagei, current support language s AR')
    translated_text = fields.CharField()
    class Meta:      
        resource_name = 'translation'
        allowed_methods = ['get']
        include_resource_uri=False
        collection_name = 'translations'

      

    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.request.GET['orig_text']
        else:
            kwargs['pk'] = bundle_or_obj.GET['orig_text']
        
        return kwargs
    
   
    def obj_get(self, bundle, **kwargs):
        
        return {}
    
    def get_object_list(self, request):
    #go ahread return empty result. dehydrate method will take care of final output
        results = []   
        new_dict = {}
                
        results.append(new_dict)

        return results

    def obj_get_list(self, bundle, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(bundle.request)
    
    def translate(self, bundle):
        txt= bundle.request.GET['orig_text'].encode('utf-8')
        
        pipe = subprocess.Popen([JOSHUA_SCRIPT_EXECUTABLE, JOSHUA_SCRIPT_FILENAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        command_stdout=pipe.communicate(txt)[0]
        translated = command_stdout.decode(encoding='utf8')
        
        return translated;
    
    def dehydrate(self, bundle):
        bundle.data['orig_text']=bundle.request.GET['orig_text']
        # bundle.data['orig_language']=bundle.request.GET['orig_language']
        bundle.data['translated_text']=self.translate(bundle)
        return bundle;
    
