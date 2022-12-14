
import sys
import socket
from datetime import datetime

def scan(target):
    #open a file and append the results
    #f = open(target + "scan_results.txt","a")
    #f.write("<p>" + "-" * 50 + "</p>")
    #f.write("<p> Scanning Target: " + target + "</p>")
    #f.write("<p> Scanning started at:" + str(datetime.now()) + "</p>")
    #f.write("<p> " + "-" * 50 +"</p>")






    f = open("scans/"+target + "scan_results.html","w")
    f.write("<html><head><title>Scan Results</title></head><body>")
    f.write("<p>" + "-" * 50 + "</p>")
    f.write("<p> Scanning Target: " + target + "</p>")
    f.write("<p> Scanning started at:" + str(datetime.now()) + "</p>")
    f.write("<p> " + "-" * 50 +"</p>")
    f.write("<p> Open Ports: </p>")
    try:
        
        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                f.write("<p>Port {} is open</p>".format(port))
                
            s.close()
            
    except socket.gaierror:
            f.write("<p> Hostname Could Not Be Resolved !!!!</p>")
            
            
    except socket.error:
            f.write("<p> Could not connect to server !!!!</p>")
            
    f.write("<p> " + "-" * 50 +"</p>")
    f.write("<p> Scanning finished at:" + str(datetime.now()) + "</p>")
    f.write("<p>" + "-" * 50 + "</p>")
    f.write("</body></html>")


    #f.close()
    return f
            




    