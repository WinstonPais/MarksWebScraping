#imports
from selenium import webdriver
import os
import xlwt
from mainApp.resultsetcustom import getrs
# from resultsetcustom import getrs

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
workbook = xlwt.Workbook()

#Setting up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])#to remove the "Chrome is being controlled by automated test software" notification
chrome_options.add_argument("--headless")#To make The Browser not appear / Headless Chrome
currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__))
chromeDriverUrl=os.path.join(currentWorkingDirectory,"chromedriver_win32")#use join function so that it works in any OS
chromeDriverUrl=os.path.join(chromeDriverUrl,"chromedriver.exe")
driver = webdriver.Chrome(chromeDriverUrl,options=chrome_options)

def getdetails(tabletag):
    # print("reached the function")
    allTRsinTable=tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
    # print(len(tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")))
    marksList=[]
    for trs in range(1,10):
        marksList.append(allTRsinTable[trs].find_elements_by_xpath("*")[2].text)
        marksList.append(allTRsinTable[trs].find_elements_by_xpath("*")[3].text)
        marksList.append(allTRsinTable[trs].find_elements_by_xpath("*")[4].text)
        marksList.append(allTRsinTable[trs].find_elements_by_xpath("*")[8].text)
    totalM=allTRsinTable[10].find_elements_by_xpath("*")[1].text
    return totalM
    # print(marksList)

def getSubjectsSemOneToFour(tabletag,semester):
    semdict={1:"I",2:"II",3:"III",4:"IV"}
    allTRsinTable=tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
    subList=[]
    for trs in range(1,10):
        subList.append(allTRsinTable[trs].find_elements_by_xpath("*")[0].text)
        subList.append(allTRsinTable[trs].find_elements_by_xpath("*")[1].text)
    sheet = workbook.add_sheet(str(semdict[semester])+" Sem")
    style = xlwt.easyxf('font: bold 1')
    sheet.write(0, 0, 'Sl. No.', style)
    sheet.write(0, 1, 'USN', style)
    sheet.write(0, 2, 'NAME', style)
    col=3
    for x in range(0,18,2):
        sheet.write(0, col, subList[x], style)
        sheet.write(1, col, subList[x+1], style)
        col+=1







# Specifying style


# Specifying column



    # print(subList)

def getSemRes(usnYear,semester,numberOfStudents):
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
        if num==1 and semester<5:
            getSubjectsSemOneToFour(driver.find_element_by_class_name("table"),semester)
        try:
            #to get the name and USN
            usnAndNameDiv=driver.find_element_by_class_name("student_details").find_elements_by_xpath("*")
            studentName=str(usnAndNameDiv[0].text)[11:] #slicing the string to remove unwanted conent / the 0th index contains the name
            resultString+=studentName+" "
            studentUSN=str(usnAndNameDiv[1].text)[13:] #slicing the string to remove unwanted conent / the 1st index contains the USN
            resultString+=studentUSN+"\n"
            #To get All Subject Marks
            resultString+=(driver.find_element_by_class_name("table").text)+"\n"
            totalM=getdetails(driver.find_element_by_class_name("table"))
            '''
                Entering Details into Excel
            '''
            slNo=1

            # for subb in range()



        except:
            # print("no data available for "+str(num))
            resultString+="no data available for "+str(num)+"\n"
        #print("-------------------------------------------------------------------")
        resultString+="-------------------------------------------------------------------\n"

    driver.close
    workbook.save("sample.xls")
    return resultString

# print(getSemRes(17,4,1))
