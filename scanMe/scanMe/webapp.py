from django.shortcuts import render

def button(request):

    return render(request,'scanMe.html')

def output(request):
    
    output_data = ""
    website_link = ""
    
    return render(request,"scanMe.html",{"output_data":output_data, "website_link":website_link})
    