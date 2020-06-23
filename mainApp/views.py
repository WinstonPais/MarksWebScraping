from django.shortcuts import render
from . import forms
from mainApp.mainScrapingCode import getSemRes
from django.core.files import File

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
    # if this is a POST request we need to process the form data
    if req.method=='POST':
        year=req.POST['year']
        sem=req.POST['semester']
        noOfS=req.POST['noOfS']
        noOfD = req.POST['noOfD']

    resultString,filename=getSemRes(int(year),int(sem),int(noOfS),int(noOfD))
    print(resultString)
    myDict={'requestedresulthere':str(resultString),'file':'excelfiles/'+str(filename)}
    return render(req,'mainApp/result.html',context=myDict)

def resultTrial(req):
    s="ANANYA G 4SO17CS001\nCode Subject name Internal External Total Credits Grade Points Grade 17CS51 MGMT. AND ENTREPRENEURSHIP FOR IT INDUSTRY 39 37 76 4 8 B P 17CS52 COMPUTER NETWORKS 36 46 82 4 9 A P 17CS553 ADVANCED JAVA AND J2EE 35 44 79 3 8 B P 17CS53 DATABASE MANAGEMENT SYSTEM 30 32 62 4 7 C P 17CS564 .NET FRAMEWORK FOR APPLICATION DEVELOPMENT 35 43 78 3 8 B P 17CS54 AUTOMATA THEORY AND COMPUTABILITY 28 32 60 4 7 C P 17CSL57 COMPUTER NETWORK LABORATORY 33 50 83 2 9 A P 17CSL58 DBMS LABORATORY WITH MINI PROJECT 35 51 86 2 9 A P TOTAL : 606 208\n-------------------------------------------------------------------\nABIGAIL JANICE TAURO 4SO17CS002\nCode Subject name Internal External Total Credits Grade Points Grade 17CS51 MGMT. AND ENTREPRENEURSHIP FOR IT INDUSTRY 39 35 74 4 8 B P 17CS52 COMPUTER NETWORKS 28 41 69 4 7 C P 17CS562 ARTIFICIAL INTELLIGENCE 32 23 55 3 6 D P 17CS53 DATABASE MANAGEMENT SYSTEM 34 30 64 4 7 C P 17CS553 ADVANCED JAVA AND J2EE 32 43 75 3 8 B P 17CS54 AUTOMATA THEORY AND COMPUTABILITY 31 21 52 4 6 D P 17CSL57 COMPUTER NETWORK LABORATORY 36 48 84 2 9 A P 17CSL58 DBMS LABORATORY WITH MINI PROJECT 35 51 86 2 9 A P TOTAL : 559 190\n-------------------------------------------------------------------\nno data available for 3\n-------------------------------------------------------------------\nADIMAYA PAI 4SO17CS004\nCode Subject name Internal External Total Credits Grade Points Grade 17CS51 MGMT. AND ENTREPRENEURSHIP FOR IT INDUSTRY 39 43 82 4 9 A P 17CS562 ARTIFICIAL INTELLIGENCE 35 38 73 3 8 B P 17CS52 COMPUTER NETWORKS 36 43 79 4 8 B P 17CS553 ADVANCED JAVA AND J2EE 37 45 82 3 9 A P 17CS53 DATABASE MANAGEMENT SYSTEM 38 42 80 4 9 A P 17CS54 AUTOMATA THEORY AND COMPUTABILITY 35 39 74 4 8 B P 17CSL57 COMPUTER NETWORK LABORATORY 38 53 91 2 10 S P 17CSL58 DBMS LABORATORY WITH MINI PROJECT 37 47 84 2 9 A P TOTAL : 645 225\n-------------------------------------------------------------------\nAJAY M KAMATH 4SO17CS005\nCode Subject name Internal External Total Credits Grade Points Grade 17CS51 MGMT. AND ENTREPRENEURSHIP FOR IT INDUSTRY 39 29 68 4 7 C P 17CS52 COMPUTER NETWORKS 33 40 73 4 8 B P 17CS562 ARTIFICIAL INTELLIGENCE 30 30 60 3 7 C P 17CS553 ADVANCED JAVA AND J2EE 31 36 67 3 7 C P 17CS53 DATABASE MANAGEMENT SYSTEM 32 23 55 4 6 D P 17CS54 AUTOMATA THEORY AND COMPUTABILITY 28 28 56 4 6 D P 17CSL57 COMPUTER NETWORK LABORATORY 36 50 86 2 9 A P 17CSL58 DBMS LABORATORY WITH MINI PROJECT 38 54 92 2 10 S P TOTAL : 557 188\n-------------------------------------------------------------------\nANCHITA PEREIRA 4SO18CS400\nCode Subject name Internal External Total Credits Grade Points Grade 17CS51 MGMT. AND ENTREPRENEURSHIP FOR IT INDUSTRY 36 45 81 4 9 A P 17ME562 ENERGY AND ENVIRONMENT 36 40 76 3 8 B P 17CS552 INTRODUCTION TO SOFTWARE TESTING 37 35 72 3 8 B P 17CS52 COMPUTER NETWORKS 24 42 66 4 7 C P 17CS53 DATABASE MANAGEMENT SYSTEM 26 35 61 4 7 C P 17CS54 AUTOMATA THEORY AND COMPUTABILITY 19 21 40 4 4 E P 17CSL57 COMPUTER NETWORK LABORATORY 20 24 44 2 4 E P 17CSL58 DBMS LABORATORY WITH MINI PROJECT 31 30 61 2 7 C P TOTAL : 501 178\n-------------------------------------------------------------------\nDEEPA TOPPO 4SO18CS401\nCode Subject name Internal External Total Credits Grade Points Grade 17CS51 MGMT. AND ENTREPRENEURSHIP FOR IT INDUSTRY 27 33 60 4 7 C P 17CV562 SUSTAINABILITY CONCEPTS IN ENGINEERING 37 24 61 3 7 C P 17CS552 INTRODUCTION TO SOFTWARE TESTING 31 22 53 3 6 D P 17CS52 COMPUTER NETWORKS 17 18 35 4 0 F F 17CS53 DATABASE MANAGEMENT SYSTEM 22 21 43 4 4 E P 17CS54 AUTOMATA THEORY AND COMPUTABILITY 20 12 32 4 0 F F 17CSL57 COMPUTER NETWORK LABORATORY 23 24 47 2 6 D P 17CSL58 DBMS LABORATORY WITH MINI PROJECT 28 30 58 2 6 D P TOTAL : 389 107\n-------------------------------------------------------------------\n"


    return render(req,'mainApp/ResultTrial.html')
