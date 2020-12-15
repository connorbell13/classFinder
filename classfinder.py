from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class classBot:

    def __init__ (self, myClassSubject, myClassNumber):
               
        #lines 11-18 open the catalog and list of all options of the class you selected
        self.driver = webdriver.Chrome()
        self.Subject = myClassSubject
        self.Number = myClassNumber
        self.driver.get("https://webapp4.asu.edu/catalog/")
        sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="subjectEntry"]').send_keys(self.Subject)
        self.driver.find_element_by_xpath('//*[@id="catNbr"]').send_keys(self.Number)
        self.driver.find_element_by_xpath('//*[@id="go_and_search"]').click()
        sleep(2)

       
        #23: gets the url of the searched class page
        myUrl= self.driver.page_source
        #25-27: downloads the web page and stores it


        #html parsing
        page_soup = soup(myUrl,"html.parser")
        


        NumClasses= page_soup.findAll('div',{"style":"vertical-align: top; font-size: smaller"})
        NumbClassesStr= str(NumClasses)
        numLine= NumbClassesStr.split('\n')
        for x in numLine:
            st=x.strip()
            break
        st=st[len(st)-3:len(st)]
        NumClassesInt=int(st.strip())
        
        #finding initial teacher
        containers= page_soup.findAll('tr',{"id":"informal"})
        #adding the rest of the teachers
        x=0
        informalNum=0
        for x in range(0,NumClassesInt):
            informalNumber= 'informal_'+str(informalNum)
            containers+=page_soup.findAll('tr',{"id":informalNumber})
            x+=1
            informalNum+=1

        #creating a str list of the teachers 'tr' files
        results=[]
        for teachers in containers:
            results.append(str(teachers))
        
        
        #Adding names to a list by calling getfirstline and getProfName to just get their names
        profNameList=[]
        for x in results:
            firstline= self.getfirstline(x)
            ProfName=self.getProfName(firstline)
            if ProfName != ' ':
                profNameList.append(ProfName)
            
        #printing list of all teacher names
        print(profNameList)





    #First Line Splitter 
    def getfirstline(self,result):
        lubes= result.split('\n')
        for x in lubes:
            st=x.strip()
            break
        return st
    

    #first name getter
    def getProfName(self, line):
        count=0
        firstdash=0
        lastdash=50
        location=0
        #finding the location of the name, will use this to get the substring of the name.
        for x in line:
            if x=='-':
                count +=1
            if count==3:
                firstdash= location
            if count==5:
                lastdash=location
            location+=1
            if location==lastdash:
                break
        #getting substring of the name and returning it
        name= line[firstdash+2:lastdash+1]
        name=name.replace('-',' ')
        return name
    
  

#entering class subject and number for the computer to run the program for:
myClassSubject = 'MAT'
myClassNumber  = '343'
myBot= classBot(myClassSubject,myClassNumber)
