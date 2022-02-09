from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, Dipendra')

# Create your views here.
