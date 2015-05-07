from django.shortcuts import  render_to_response
from Joshua import settings


# Create your views here.

def home(request):
    context = {'JOSHUA_WEB_API_URL': settings.JOSHUA_WEB_API_URL}
    return render_to_response( 'home.html', context)
    # return render(request, 'home.html')