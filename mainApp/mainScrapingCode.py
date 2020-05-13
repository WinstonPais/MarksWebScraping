#imports
from selenium import webdriver
import os
import xlwt
from mainApp.resultsetcustom import getrs,getrs1
from time import sleep
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
driver.maximize_window()
driver.implicitly_wait(30)

def getdetailsYearTwo(tabletag,sheet,num,url,semester):
    if url.find("cs4")!=-1 and semester==4 :
        allTRsinTable=tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
        styleTNR12 = xlwt.easyxf("font: name Times New Roman, height 240;"
                                 "align:vertical center, horizontal center;")
        marksList=[]
        colVal=3
        for trs in range(1,len(allTRsinTable)-1):
            sheet.write(num+1, colVal, allTRsinTable[trs].find_elements_by_xpath("*")[2].text, styleTNR12)
            sheet.write(num+1, colVal+1, allTRsinTable[trs].find_elements_by_xpath("*")[3].text, styleTNR12)
            sheet.write(num+1, colVal+2, allTRsinTable[trs].find_elements_by_xpath("*")[4].text, styleTNR12)
            sheet.write(num+1, colVal+3, allTRsinTable[trs].find_elements_by_xpath("*")[8].text, styleTNR12)
            colVal+=7
        sheet.write(num+1, colVal, allTRsinTable[-1].find_elements_by_xpath("*")[1].text, styleTNR12)
    elif semester == 4:
        allTRsinTable = tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
        styleTNR12 = xlwt.easyxf("font: name Times New Roman, height 240;"
                                 "align:vertical center, horizontal center;")
        marksList = []
        colVal = 10
        for trs in range(1, len(allTRsinTable) - 1):
            sheet.write(num + 1, colVal, allTRsinTable[trs].find_elements_by_xpath("*")[2].text, styleTNR12)
            sheet.write(num + 1, colVal + 1, allTRsinTable[trs].find_elements_by_xpath("*")[3].text, styleTNR12)
            sheet.write(num + 1, colVal + 2, allTRsinTable[trs].find_elements_by_xpath("*")[4].text, styleTNR12)
            sheet.write(num + 1, colVal + 3, allTRsinTable[trs].find_elements_by_xpath("*")[8].text, styleTNR12)
            colVal += 7
        sheet.write(num + 1, colVal, allTRsinTable[-1].find_elements_by_xpath("*")[1].text, styleTNR12)
    elif url.find("cs4")!= -1 and semester == 3:
        allTRsinTable = tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
        styleTNR12 = xlwt.easyxf("font: name Times New Roman, height 240;"
                                 "align:vertical center, horizontal center;")
        marksList = []
        colVal = 3
        for trs in range(1, len(allTRsinTable) - 1):
            sheet.write(num + 1, colVal, allTRsinTable[trs].find_elements_by_xpath("*")[2].text, styleTNR12)
            sheet.write(num + 1, colVal + 1, allTRsinTable[trs].find_elements_by_xpath("*")[3].text, styleTNR12)
            sheet.write(num + 1, colVal + 2, allTRsinTable[trs].find_elements_by_xpath("*")[4].text, styleTNR12)
            sheet.write(num + 1, colVal + 3, allTRsinTable[trs].find_elements_by_xpath("*")[8].text, styleTNR12)
            colVal += 7
        sheet.write(num + 1, colVal, allTRsinTable[-1].find_elements_by_xpath("*")[1].text, styleTNR12)
    elif url.find("cs0")!=-1 or url.find("cs1")!=-1 and semester==3:
        allTRsinTable = tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
        styleTNR12 = xlwt.easyxf("font: name Times New Roman, height 240;"
                                 "align:vertical center, horizontal center;")
        marksList = []
        colVal=3
        sheet.write(num+1,colVal,allTRsinTable[1].find_elements_by_xpath("*")[2].text,styleTNR12)
        sheet.write(num+1,colVal+1,allTRsinTable[1].find_elements_by_xpath("*")[3].text,styleTNR12)
        sheet.write(num+1,colVal+2,allTRsinTable[1].find_elements_by_xpath("*")[4].text,styleTNR12)
        sheet.write(num+1, colVal+3, allTRsinTable[1].find_elements_by_xpath("*")[8].text,styleTNR12)
        colVal=17
        for trs in range(2, len(allTRsinTable) - 1):
            sheet.write(num + 1, colVal, allTRsinTable[trs].find_elements_by_xpath("*")[2].text, styleTNR12)
            sheet.write(num + 1, colVal + 1, allTRsinTable[trs].find_elements_by_xpath("*")[3].text, styleTNR12)
            sheet.write(num + 1, colVal + 2, allTRsinTable[trs].find_elements_by_xpath("*")[4].text, styleTNR12)
            sheet.write(num + 1, colVal + 3, allTRsinTable[trs].find_elements_by_xpath("*")[8].text, styleTNR12)
            colVal += 7
        sheet.write(num + 1, colVal, allTRsinTable[-1].find_elements_by_xpath("*")[1].text, styleTNR12)
    else:
        allTRsinTable = tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
        styleTNR12 = xlwt.easyxf("font: name Times New Roman, height 240;"
                                 "align:vertical center, horizontal center;")
        marksList = []
        colVal = 3
        for trs in range(1, len(allTRsinTable) - 1):
            sheet.write(num + 1, colVal, allTRsinTable[trs].find_elements_by_xpath("*")[2].text, styleTNR12)
            sheet.write(num + 1, colVal + 1, allTRsinTable[trs].find_elements_by_xpath("*")[3].text, styleTNR12)
            sheet.write(num + 1, colVal + 2, allTRsinTable[trs].find_elements_by_xpath("*")[4].text, styleTNR12)
            sheet.write(num + 1, colVal + 3, allTRsinTable[trs].find_elements_by_xpath("*")[8].text, styleTNR12)
            colVal += 7
        sheet.write(num + 1, colVal, allTRsinTable[-1].find_elements_by_xpath("*")[1].text, styleTNR12)

def getSubjectsYearTwoHeadings(tabletag,semester,sheet):
        allTRsinTable=tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
        subList=[]
        for trs in range(1,len(allTRsinTable)-1):
            subList.append(allTRsinTable[trs].find_elements_by_xpath("*")[1].text)

        styleTNR12 = xlwt.easyxf("font: name Times New Roman, bold 1,height 240;"
                                 "align:vertical center, horizontal center;")
        styleC12 = xlwt.easyxf("font: name Calibri, bold 1,height 220;"
                               "align:vertical center, horizontal center")#height 20 means 1 in excel
        styleC11Yellow = xlwt.easyxf(#"pattern: pattern solid,back_color red;"
                                "font: name Calibri, bold 1,height 220;"
                                 "align:vertical center, horizontal center;")

        sheet.write_merge(0, 1, 1, 1, 'USN', styleTNR12)   #(top_row, bottom_row, left_column, right_column,content,style)
        sheet.write_merge(0, 1, 2, 2, 'NAME', styleTNR12)
        colVal=3
        for index in range(0,len(subList)):
            sheet.write_merge(0, 0, colVal, colVal+3, subList[index], styleC12)
            sheet.write(1, colVal, 'Int', styleC12)
            sheet.write(1, colVal+1, 'Ext', styleC12)
            sheet.write(1, colVal+2, 'Total', styleC12)
            sheet.write(1, colVal+3, 'Result', styleC12)
            sheet.write_merge(0, 0, colVal+4, colVal+6, "Revaluvation", styleC11Yellow)
            sheet.write(1, colVal+4, 'Ext',styleC11Yellow)
            sheet.write(1, colVal+5, 'Total',styleC11Yellow)
            sheet.write(1, colVal+6, 'Result',styleC11Yellow)
            colVal+=7
        sheet.write_merge(0, 1, colVal, colVal, "Total", styleC12)

def yearThree(tabletag,sheet,y3Sub,num,y3total):
    styleTNR12 = xlwt.easyxf("font: name Times New Roman, bold 1,height 240;"
                             "align:vertical center, horizontal center;")
    styleC12 = xlwt.easyxf("font: name Calibri, bold 1,height 220;"
                           "align:vertical center, horizontal center")#height 20 means 1 in excel
    styleC11Yellow = xlwt.easyxf(#"pattern: pattern solid,back_color red;"
                            "font: name Calibri, bold 1,height 220;"
                             "align:vertical center, horizontal center;")
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
            sheet.write_merge(0, 0, ind*7+3+4, ind*7+3+6, "Revaluvation", styleC11Yellow)
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
    semdict={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII"}
    sheet = workbook.add_sheet(str(semdict[semester])+" Sem",cell_overwrite_ok=True)
    rs=getrs(usnYear,semester)
    urlPart2 = "/sem-"+str(semester)+"/rs-"+str(rs)+"?cbse=1"
    urlPart3 = "https://www.vtu4u.com/result/4so"+str(usnYear)
    urlPart1 = "https://www.vtu4u.com/result/4so" + str(usnYear+1)
    resultString = ""
    url1=urlPart1+"cs400"+urlPart2
    driver.get(url1)
    sleep(1)
    if semester == 3 or semester == 4:
        getSubjectsYearTwoHeadings(driver.find_element_by_class_name("table"), semester, sheet)
    if semester==5 or semester==6:
        sheet.write_merge(0, 1, 1, 1, 'USN', styleTNR12B)   #(top_row, bottom_row, left_column, right_column,content,style)
        sheet.write_merge(0, 1, 2, 2, 'NAME', styleTNR12B)
        y3Sub=[]
        y3total=[]

    num2=1
    for num in range(1,(numberOfStudents+1)):
        if num<10:
            url = urlPart3+"cs00"+str(num)+urlPart2
        elif num<100:
            url = urlPart3+"cs0"+str(num)+urlPart2
        else:
            url = urlPart3+"cs"+str(num)+urlPart2
        driver.get(url)

        try:
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
            # totalM=getdetails(driver.find_element_by_class_name("table"))

            if semester==3 or semester==4:
                getdetailsYearTwo(driver.find_element_by_class_name("table"),sheet,num,url,semester)
            if semester==5 or semester==6:
                yearThree(driver.find_element_by_class_name("table"),sheet,y3Sub,num,y3total)
        except:
            # print("no data available for "+str(num))
            resultString+="no data available for "+str(num)+"\n"
            sheet.write(num+1,2,"no data available for "+str(num),styleTNR12)
            if semester==5 or semester==6:
                y3total.append("0")
        #print("-------------------------------------------------------------------")
        resultString+="-------------------------------------------------------------------\n"

    rs = getrs1(usnYear+1, semester)
    for num in range(0,(numberOfDiplomas)):
        if num<10:
            url=urlPart1+"cs40"+str(num)+urlPart2
        else:
            url=urlPart1+"cs4"+str(num)+urlPart2
        driver.get(url)

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
            # totalM=getdetails(driver.find_element_by_class_name("table"))

            if semester==3 or semester==4:
                getdetailsYearTwo(driver.find_element_by_class_name("table"),sheet,numberOfStudents+num+1,url,semester)
            if semester==5 or semester==6:
                yearThree(driver.find_element_by_class_name("table"),sheet,y3Sub,numberOfStudents+num+1,y3total)



        except:
            # print("no data available for "+str(num))
            resultString+="no data available for "+str(num)+"\n"
            sheet.write(num+2,2,"no data available for "+str(num),styleTNR12)
            if semester==5 or semester==6:
                y3total.append("0")
        #print("-------------------------------------------------------------------")
        resultString+="-------------------------------------------------------------------\n"

    if semester==5 or semester==6:
        sheet.write_merge(0, 1, len(y3Sub)*7+3, len(y3Sub)*7+3, "Total", styleC12)
        for m in range(0,len(y3total)):
            sheet.write(m+2, len(y3Sub)*7+3, y3total[m], styleTNR12)

    driver.close
    workbook.save("4SO"+str(usnYear)+"CS-SEM-"+str(semester)+".xls")
    return resultString

# print(getSemRes(17,4,1))
