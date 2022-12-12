
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






    f = open(target + "scan_results.txt","w")
    f.write("-" * 50 + "\n")
    f.write("Scanning Target: " + target + "\n")
    f.write("Scanning started at:" + str(datetime.now()) + "\n")
    f.write("-" * 50 +"\n")
    try:
        
        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                f.write("Port {} is open".format(port) + "\n")
            s.close()
            
    except socket.gaierror:
            f.write("\n Hostname Could Not Be Resolved !!!!")
            
    except socket.error:
            f.write("\ Server not responding !!!!")


    #f.close()
    return f
            




    