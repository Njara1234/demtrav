from django.http import HttpResponse
from django.shortcuts import render
from web.models import Flight

# Create your views here.
def index(request):

   context = {
      "vol": Flight.objects.all(),
      "developer":"Rambo"
   }

   
   # return HttpResponse ("hello, hello")
   return render(request, "flights/index.html",context)

def about(request):
   # return HttpResponse ("hello, hello")
   return render(request, "about/index.html")