from selenium import webdriver
import os
import xlwt
from mainApp.resultsetcustom import getrs
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import platform
# from resultsetcustom import getrs

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xlwt.add_palette_colour("custom_colour", 0x21)
xlwt.add_palette_colour("custom_colour1", 0x22)
borders= xlwt.Borders()
workbook = xlwt.Workbook()
workbook.set_colour_RGB(0x21, 255, 255, 0) #Excel cell color(yellow)
workbook.set_colour_RGB(0x22, 245, 245, 245)  #Excel cell color(grey)

#Setting up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])#to remove the "Chrome is being controlled by automated test software" notification
chrome_options.add_argument("--headless")#To make The Browser not appear / Headless Chrome
currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__))
if platform.system() == 'Linux':
    chromeDriverUrl=os.path.join(currentWorkingDirectory,"chromedriver_linux64")
else:
    chromeDriverUrl=os.path.join(currentWorkingDirectory,"chromedriver_win32")#use join function so that it works in any OS
chromeDriverUrl=os.path.join(chromeDriverUrl,"chromedriver.exe")
driver = webdriver.Chrome(executable_path=str(chromeDriverUrl),options=chrome_options)

def yearThree(tabletag,sheet,y3Sub,num,y3total):
    styleTNR12 = xlwt.easyxf("font: name Times New Roman, bold 1,height 240;"
                             "align:vertical center, horizontal center;")
    styleC12 = xlwt.easyxf("font: name Calibri, bold 1,height 220;"
                           "align:vertical center, horizontal center;")#height 20 means 1 in excel
    styleC11Yellow = xlwt.easyxf(
        "font: name Calibri, bold 1,height 220;"
        "align:vertical center, horizontal center;"
        "pattern: pattern solid, fore_colour custom_colour;"
        "borders: top_color black, bottom_color black, right_color black, left_color black,left thin, right thin, top thin, bottom thin;")
    allTRsinTable=tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
    for trs in range(1,len(allTRsinTable)-1):
        cSub=allTRsinTable[trs].find_elements_by_xpath("*")[1].text
        if cSub in y3Sub:
            ind=y3Sub.index(cSub)
            sheet.write(num+1, ind*7+3, allTRsinTable[trs].find_elements_by_xpath("*")[2].text, styleTNR12)
            sheet.write(num+1, ind*7+3+1, allTRsinTable[trs].find_elements_by_xpath("*")[3].text, styleTNR12)
            sheet.write(num+1, ind*7+3+2, allTRsinTable[trs].find_elements_by_xpath("*")[4].text, styleTNR12)
            sheet.write(num+1, ind*7+3+3, allTRsinTable[trs].find_elements_by_xpath("*")[8].text, styleTNR12)
        else:
            #add new subject to the list of subjects
            y3Sub.append(cSub)
            ind=y3Sub.index(cSub)
            #add the new subject as a heading in the excel sheet
            sheet.write_merge(0, 0, ind*7+3, ind*7+6, cSub, styleC12)
            sheet.write(1, ind*7+3, 'Int', styleC12)
            sheet.write(1, ind*7+3+1, 'Ext', styleC12)
            sheet.write(1, ind*7+3+2, 'Total', styleC12)
            sheet.write(1, ind*7+3+3, 'Result', styleC12)
            sheet.write_merge(0, 0, ind*7+3+4, ind*7+3+6, "Revaluation", styleC11Yellow)
            sheet.write(1, ind*7+3+4, 'Ext',styleC11Yellow)
            sheet.write(1, ind*7+3+5, 'Total',styleC11Yellow)
            sheet.write(1, ind*7+3+6, 'Result',styleC11Yellow)
            #add the current students marks into the excel add_sheet
            sheet.write(num+1, ind*7+3, allTRsinTable[trs].find_elements_by_xpath("*")[2].text, styleTNR12)
            sheet.write(num+1, ind*7+3+1, allTRsinTable[trs].find_elements_by_xpath("*")[3].text, styleTNR12)
            sheet.write(num+1, ind*7+3+2, allTRsinTable[trs].find_elements_by_xpath("*")[4].text, styleTNR12)
            sheet.write(num+1, ind*7+3+3, allTRsinTable[trs].find_elements_by_xpath("*")[8].text, styleTNR12)
    y3total.append(allTRsinTable[-1].find_elements_by_xpath("*")[1].text)

def getSemRes(usnYear,semester,numberOfStudents,numberOfDiplomas):
    styleC12 = xlwt.easyxf("font: name Calibri, bold 1,height 220;"
                           "align:vertical center, horizontal center")
    styleTNR12 = xlwt.easyxf("font: name Times New Roman, height 240;"
                             "align:vertical center, horizontal center;")
    styleTNR12B = xlwt.easyxf("font: name Times New Roman, bold 1,height 240;"
                             "align:vertical center, horizontal center;")
    styleTNR12E = xlwt.easyxf("font: name Times New Roman, height 240, colour red;"
                             "align:vertical center, horizontal center;"
                             "pattern: pattern solid, fore_colour custom_colour1;")
    semdict={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII"}
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    sheet = workbook.add_sheet(str(semdict[semester])+"_Sem_"+str(dt_string),cell_overwrite_ok=True)
    col_width1 = 256 * 20
    col_width2 = 256 * 25
    rs=getrs(usnYear,semester)
    urlPart2 = "/sem-"+str(semester)+"/rs-"+str(rs)+"?cbse=1"
    urlPart3 = "https://www.vtu4u.com/result/4so"+str(usnYear)
    urlPart1 = "https://www.vtu4u.com/result/4so" + str(usnYear+1)
    resultString = ""
    for num in range(1,(numberOfStudents+1)):
        if num<10:
            url = urlPart3+"cs00"+str(num)+urlPart2
        elif num<100:
            url = urlPart3+"cs0"+str(num)+urlPart2
        else:
            url = urlPart3+"cs"+str(num)+urlPart2
        driver.get(url)
        sleep(2)
        print(url)
        try:
            if num ==1:
                    sheet.write_merge(0, 1, 1, 1, 'USN', styleTNR12B)   #(top_row, bottom_row, left_column, right_column,content,style)
                    sheet.col(1).width=col_width1
                    sheet.write_merge(0, 1, 2, 2, 'NAME', styleTNR12B)
                    sheet.col(2).width = col_width2
                    y3Sub=[]
                    y3total=[]
            #to get the name and USN
            usnAndNameDiv=driver.find_element_by_class_name("student_details").find_elements_by_xpath("*")
            studentName=str(usnAndNameDiv[0].text)[11:] #slicing the string to remove unwanted conent / the 0th index contains the name
            resultString+=studentName+" "
            studentUSN=str(usnAndNameDiv[1].text)[13:] #slicing the string to remove unwanted conent / the 1st index contains the USN
            resultString+=studentUSN+"\n"
            sheet.write(num+1,1,studentUSN,styleTNR12)
            sheet.write(num+1,2,studentName,styleTNR12)
            #To get All Subject Marks
            resultString+=(driver.find_element_by_class_name("table").text)+"\n"
            yearThree(driver.find_element_by_class_name("table"),sheet,y3Sub,num,y3total)
        except:
            resultString+="no data available for "+str(num)+"\n"
            sheet.write(num+1,2,"No data available for "+str(num),styleTNR12E)
            y3total.append("0")
        resultString+="-------------------------------------------------------------------\n"

    for num in range(0,(numberOfDiplomas)):
        if num<10:
            url=urlPart1+"cs40"+str(num)+urlPart2
        else:
            url=urlPart1+"cs4"+str(num)+urlPart2
        driver.get(url)
        sleep(2)
        try:
            #to get the name and USN
            usnAndNameDiv=driver.find_element_by_class_name("student_details").find_elements_by_xpath("*")
            studentName=str(usnAndNameDiv[0].text)[11:] #slicing the string to remove unwanted conent / the 0th index contains the name
            resultString+=studentName+" "
            studentUSN=str(usnAndNameDiv[1].text)[13:] #slicing the string to remove unwanted conent / the 1st index contains the USN
            resultString+=studentUSN+"\n"
            sheet.write(numberOfStudents+num+2,1,studentUSN,styleTNR12)
            sheet.write(numberOfStudents+num+2,2,studentName,styleTNR12)
            #To get All Subject Marks
            resultString+=(driver.find_element_by_class_name("table").text)+"\n"
            yearThree(driver.find_element_by_class_name("table"),sheet,y3Sub,numberOfStudents+num+1,y3total)



        except:
            resultString+="no data available for "+str(400+num)+"\n"
            sheet.write(numberOfStudents+num+2,2,"No data available for "+str(400+num),styleTNR12E)
            y3total.append("0")
        resultString+="-------------------------------------------------------------------\n"

    sheet.write_merge(0, 1, len(y3Sub)*7+3, len(y3Sub)*7+3, "Total", styleC12)
    for m in range(0,len(y3total)):
        sheet.write(m+2, len(y3Sub)*7+3, y3total[m], styleTNR12)

    driver.close

    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    finalFileName = "4SO"+str(usnYear)+"CS-SEM-"+str(semester)+"-"+str(dt_string)+".xls"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    EXCEL_DIR=os.path.join(os.path.join(BASE_DIR,"static"),"excelfiles")
    workbook.save(os.path.join(EXCEL_DIR,finalFileName))
    return resultString,finalFileName
