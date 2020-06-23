from django.shortcuts import render
from . import forms
from mainApp.mainScrapingCode import getSemRes
from django.core.files import File
from mainApp.SplitString import getdata,getNameUsn

# Create your views here.
def index(req):
    return render(req,'mainapp/index.html')

def inputpage(req):
    return render(req,'mainApp/inputPage.html')

def index(req):
    return render(req,'mainApp/index.html')

def contact(req):
    return render(req,'mainApp/contact.html')

def result(req):
    if req.method=='POST':
        year=req.POST['year']
        sem=req.POST['semester']
        noOfS=req.POST['noOfS']
        noOfD = req.POST['noOfD']

    resultString,filename=getSemRes(int(year),int(sem),int(noOfS),int(noOfD))
    usnList,nameList = getNameUsn(resultString)
    studentdataList = getdata(resultString)
    myDict={'usnList':usnList,'studentdataList':studentdataList,'nameList':nameList,'file':'excelfiles/'+str(filename)}
    return render(req,'mainApp/Result.html',context=myDict)
