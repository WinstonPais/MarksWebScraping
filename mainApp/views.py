from django.shortcuts import render
from . import forms
from mainApp.mainScrapingCode import getSemRes

# Create your views here.
def index(req):
    return render(req,'mainapp/index.html')

def inputpage(req):
    return render(req,'mainApp/inputPage.html')

def result(req):
    # if this is a POST request we need to process the form data
    if req.method=='POST':
        year=req.POST['year']
        sem=req.POST['semester']
        noOfS=req.POST['noOfS']
        noOfD = req.POST['noOfD']
        #print(str(year)+" "+str(sem)+" "+str(noOfS))
    resultString=getSemRes(int(year),int(sem),int(noOfS),int(noOfD))
    myDict={'requestedresulthere':str(resultString)}

    return render(req,'mainApp/result.html',context=myDict)
