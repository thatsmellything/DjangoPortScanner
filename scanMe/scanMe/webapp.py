from django.shortcuts import render
from . import scanner
import time



    




def button(request):

    return render(request,'scanMe.html')

def output(request):



    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    #give time for scanner to run

    

    make_output_file = scanner.scan(ip)
    scanner.scan(ip)
    #time.sleep(10)

    output_file = open(ip + "scan_results.txt","r")

    #read the output file
    output_data = output_file.read()
    output_file.close()

    
    return render(request,"scanMe.html",{"output_data":output_data})
    