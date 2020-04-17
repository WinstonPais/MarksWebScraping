#imports
from selenium import webdriver
import os

#Setting up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])#to remove the "Chrome is being controlled by automated test software" notification
chrome_options.add_argument("--headless")#To make The Browser not appear / Headless Chrome

currentWorkingDirectory=os.path.dirname(os.path.abspath(__file__))
chromeDriverUrl=os.path.join(currentWorkingDirectory,"chromedriver_win32")#use join function so that it works in any OS
chromeDriverUrl=os.path.join(chromeDriverUrl,"chromedriver.exe")

driver = webdriver.Chrome(chromeDriverUrl,options=chrome_options)



def getrs(year,sem):
    for i in range(1,10):
        url="https://www.vtu4u.com/results/4so"+str(year)+"cs00"+str(i)+"?cbse=1"
        driver.get(url)
        allTables=driver.find_elements_by_class_name("table") #getting all tables i.e. all sem results including revaluation
        for tabletags in allTables:
            allTableRows=tabletags.find_elements_by_tag_name("tr")
            semester=allTableRows[1].find_elements_by_tag_name("td")[0].text
            sgpa=allTableRows[1].find_elements_by_tag_name("td")[3].text
            #print(semester)
           # print(sgpa)

            if int(semester)==sem and str(sgpa)!="N/A":
                #print("inside")
                hrefToMarks=allTableRows[1].find_elements_by_tag_name("td")[6].find_element_by_tag_name("a").get_attribute("href")
                rs=hrefToMarks[49:51]
                if rs[1]=="?":
                    resultSet=rs[0]
                else:
                    resultSet=rs
                #print(resultSet)
                #print(hrefToMarks)
                return resultSet

def getrs1(year,sem):
    for i in range(0,10):
        url="https://www.vtu4u.com/results/4so"+str(year)+"cs40"+str(i)+"?cbse=1"
        driver.get(url)
        allTables=driver.find_elements_by_class_name("table") #getting all tables i.e. all sem results including revaluation
        for tabletags in allTables:
            allTableRows=tabletags.find_elements_by_tag_name("tr")
            semester=allTableRows[1].find_elements_by_tag_name("td")[0].text
            sgpa=allTableRows[1].find_elements_by_tag_name("td")[3].text
            #print(semester)
           # print(sgpa)

            if int(semester)==sem and str(sgpa)!="N/A":
                #print("inside")
                hrefToMarks=allTableRows[1].find_elements_by_tag_name("td")[6].find_element_by_tag_name("a").get_attribute("href")
                rs=hrefToMarks[49:51]
                if rs[1]=="?":
                    resultSet=rs[0]
                else:
                    resultSet=rs
                #print(resultSet)
                #print(hrefToMarks)
                return resultSet

