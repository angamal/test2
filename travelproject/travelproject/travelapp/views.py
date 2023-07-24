
from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
#from.models import Places
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    #obj1=Places.objects.all()

    return render(request, "index.html",{'result':obj})
#def addition(request):
    #x=int(request.GET['num1'])
    #res=[(x+y),(x-y),(x*y),(x/y)]
    #return render(request,"result.html",{'result':res})

#def about(request):
    #return render(request,"about.html")





#def contact(request):
    #return HttpResponse("Hello am contact")