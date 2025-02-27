from django.shortcuts import render
from django.http import JsonResponse
def home(request):
    return render(request, 'index.html')

def python_funct(request):
      #do something with the data passed

      fname=request.GET.get('fname',None)
      lname=request.GET.get('lname',None)
      fullname= fname+' '+lname
      #fullname= 33
      response = {
        'fullname': fullname
         }
      return JsonResponse(response)
