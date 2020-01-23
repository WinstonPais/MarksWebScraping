#imports
from selenium import webdriver
import os
from mainApp.resultsetcustom import getrs

#Setting up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])#to remove the "Chrome is being controlled by automated test software" notification
chrome_options.add_argument("--headless")#To make The Browser not appear / Headless Chrome

currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__))
chromeDriverUrl=os.path.join(currentWorkingDirectory,"chromedriver_win32")#use join function so that it works in any OS
chromeDriverUrl=os.path.join(chromeDriverUrl,"chromedriver.exe")

driver = webdriver.Chrome(executable_path=r""+chromeDriverUrl+"",options=chrome_options)#Regular Expression for the path

def getSemRes(usnYear,semester,numberOfStudents):
    #input

    #usnYear=int(input("Enter the year:"))
    #semester=int(input("Enter the semester:"))
    #numberOfStudents=int(input("Enter the number of students:"))

    rs=getrs(usnYear,semester)

    #initialize url
    urlPart1="https://www.vtu4u.com/result/4so"+str(usnYear)
    urlPart2="/sem-"+str(semester)+"/rs-"+str(rs)+"?cbse=1"
    resultString=""
    for num in range(1,(numberOfStudents+1)):

        if num<10:
            url=urlPart1+"cs00"+str(num)+urlPart2
        elif num<100:
            url=urlPart1+"cs0"+str(num)+urlPart2
        else:
            url=urlPart1+"cs"+str(num)+urlPart2

        driver.get(url)
        try:
            #to get the name and USN
            usnAndNameDiv=driver.find_element_by_class_name("student_details").find_elements_by_xpath("*")
            studentName=str(usnAndNameDiv[0].text)[11:] #slicing the string to remove unwanted conent / the 0th index contains the name
            #print(studentName+" ",end="")
            resultString+=studentName+" "
            studentUSN=str(usnAndNameDiv[1].text)[13:] #slicing the string to remove unwanted conent / the 1st index contains the USN
            #print(studentUSN)
            resultString+=studentUSN+"\n"

            #To get All Subject Marks
            #print(driver.find_element_by_class_name("table").text)
            resultString+=(driver.find_element_by_class_name("table").text)+"\n"

        except:
            #print("no data available for "+str(num))
            resultString+="no data available for "+str(num)+"\n"
        #print("-------------------------------------------------------------------")
        resultString+="-------------------------------------------------------------------\n"

    driver.close
    return resultString
