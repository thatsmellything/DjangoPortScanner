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
    scanner.nmapScan(ip)
    #time.sleep(10)

    #output_file = open(ip + "scan_results.txt","r")

    #read the output file
    #utput_data = output_file.read()
    #output_file.close()

    #redirect to scans/IP+scan_results.html
    return render(request,ip + "scan_results.html")
    