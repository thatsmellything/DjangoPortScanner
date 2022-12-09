from django.shortcuts import render
from . import scanner



    




def button(request):

    return render(request,'scanMe.html')

def output(request):



    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    
    output_data = scanner.scan(ip)
    
    
    return render(request,"scanMe.html",{"output_data":output_data})
    