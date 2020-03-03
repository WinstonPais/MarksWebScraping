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

# def set_style(name, height, bold=False):
#     style = xlwt.XFStyle()  # 初始化样式
#
#     font = xlwt.Font()  # 为样式创建字体
#     font.name = name  # 'Times New Roman'
#     font.bold = bold
#     font.color_index = 4
#     font.height = height
#
#     # borders= xlwt.Borders()
#     # borders.left= 6
#     # borders.right= 6
#     # borders.top= 6
#     # borders.bottom= 6
#
#     style.font = font
#     # style.borders = borders
#
#     return style

def getSubjectsYearTwoHeadings(tabletag,semester):
    semdict={1:"I",2:"II",3:"III",4:"IV"}
    allTRsinTable=tabletag.find_element_by_tag_name("tbody").find_elements_by_xpath("*")
    subList=[]
    for trs in range(1,10):
        # subList.append(allTRsinTable[trs].find_elements_by_xpath("*")[0].text)
        subList.append(allTRsinTable[trs].find_elements_by_xpath("*")[1].text)
    sheet = workbook.add_sheet(str(semdict[semester])+" Sem")
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
    workbook.save("sample.xls")

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
        if num==1:
            if semester==3 or semester==4:
                getSubjectsYearTwoHeadings(driver.find_element_by_class_name("table"),semester)
        try:
            #to get the name and USN
            usnAndNameDiv=driver.find_element_by_class_name("student_details").find_elements_by_xpath("*")
            studentName=str(usnAndNameDiv[0].text)[11:] #slicing the string to remove unwanted conent / the 0th index contains the name
            resultString+=studentName+" "
            studentUSN=str(usnAndNameDiv[1].text)[13:] #slicing the string to remove unwanted conent / the 1st index contains the USN
            resultString+=studentUSN+"\n"
            #To get All Subject Marks
            resultString+=(driver.find_element_by_class_name("table").text)+"\n"
            # totalM=getdetails(driver.find_element_by_class_name("table"))
            '''
                Entering Details into Excel
            '''
            # slNo=1

            # for subb in range()



        except:
            # print("no data available for "+str(num))
            resultString+="no data available for "+str(num)+"\n"
        #print("-------------------------------------------------------------------")
        resultString+="-------------------------------------------------------------------\n"

    driver.close

    return resultString

# print(getSemRes(17,4,1))
