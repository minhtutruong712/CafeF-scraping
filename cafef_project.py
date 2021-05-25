import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\90.0.4430.85\chromedriver.exe')  
import time
from selenium import webdriver 
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import numpy as np
import json

link='https://e.cafef.vn/info.ashx?type=cp&symbol='
company=[]
list_of_link=[]
companylink=[]
list=['AAA','ANV','ASM','AST','BHN','BMP','BWE','CAV','CHP','CII','CMG','CTD','DBC','DBD','DCM','DHC','DHG', 
'DMC','DPM','DRC','DTL','DVP','FPT','GAS','GEG','GEX','GMD','GTN','GVR','HAG','HBC','HNG','HPG','HSG','HT1', 
'HVN','IDI','IMP','KDC','LGC','MSH','MSN','MWG','NCT','NKG','NT2','PAC','PAN','PC1','PGD','PHR','PLX','PME', 
'PNJ','POW','PPC','PTB','PVD','PVT','REE','ROS','SAB','SAM','SBT','SCS','SGN','SHP','TCH','TDM','TLG','TMP', 
'TRA','VCF','VGC','VHC','VIS','VJC','VNM','VSC','VSH']
for i in list:
    company.append(link+i)
for link in company:
    html=urlopen(link)
    list_of_link.append(BeautifulSoup(html.read(), 'html.parser').get_text())
for i in list_of_link:
    res=json.loads(i)
    companylink.append(res['Link'])
finance=[] 
profile=[]
cashflow=[]  
for link in companylink:
    driver.get(link)
    pages = driver.find_elements_by_xpath('//a[contains(@href, "/IncSta/")]')
    finance.append(pages[0].get_attribute('href'))
for link in finance:
    profile.append(link.replace('/IncSta/','/BSheet/'))
for link in profile:
    cashflow.append(link.replace('/BSheet/','/CashFlow/'))
#tongtaisan
tongtaisan=[]
taisan=[]
tongvonsohuu=[]
vonsohuu=[]
for html in profile: 
    html=urlopen(html)
    bs = BeautifulSoup(html.read(), 'html.parser')    
    tongtaisan.append(bs.find_all('tr', attrs={"id":"001"}))       
    tongvonsohuu.append(bs.find_all('tr', attrs={"id":"400"}))    
for sibling in tongtaisan:
    for sib in sibling:
        taisan.append(sib.find_all('td')[1:5])
taisancon=[]
for child in taisan:         
    for sib in child:        
        taisancon.append(sib.get_text())

#vonchusohuu
for sibling in tongvonsohuu:
    for sib in sibling:
        vonsohuu.append(sib.find_all('td')[1:5])
vonsohuucon=[]
for child in vonsohuu:            
    for sib in child:        
        vonsohuucon.append(sib.get_text())
        
#loinhuantruocthue
loinhuantruocthue=[]
loinhuansauthue=[]
chiphilaivay=[]
loinhuantruoc=[]
loinhuansau=[]
chiphilai=[]
for html in finance: 
    html=urlopen(html)
    bs = BeautifulSoup(html.read(), 'html.parser')    
    loinhuantruocthue.append(bs.find_all('tr', attrs={"id":"50"}))       
    loinhuansauthue.append(bs.find_all('tr', attrs={"id":"60"}))
    chiphilaivay.append(bs.find_all('tr', attrs={"id":"23"}))  
for sibling in loinhuantruocthue:
    for sib in sibling:
        loinhuantruoc.append(sib.find_all('td')[1:5])
loinhuantruoccon=[]
for child in loinhuantruoc:           
    for sib in child:        
        loinhuantruoccon.append(sib.get_text())
        
#loinhuansauthue
for sibling in loinhuansauthue:
    for sib in sibling:
        loinhuansau.append(sib.find_all('td')[1:5])
loinhuansaucon=[]
for child in loinhuansau:            
    for sib in child:        
        loinhuansaucon.append(sib.get_text())
       
#chiphilaivay
for sibling in chiphilaivay:
    for sib in sibling:
        chiphilai.append(sib.find_all('td')[1:5])
chiphilaicon=[]
for child in chiphilai:           
    for sib in child:        
        chiphilaicon.append(sib.get_text())
      
#tskhauhao
tskhauhao=[]
khauhao=[]
for html in profile: 
    html=urlopen(html)
    bs = BeautifulSoup(html.read(), 'html.parser')    
    tskhauhao.append(bs.find_all('tr', attrs={"id":"02"}))   
for sibling in tongtaisan:
    for sib in sibling:
        khauhao.append(sib.find_all('td')[1:5])
khauhaocon=[]
for child in khauhao:           
    for sib in child:        
        khauhaocon.append(sib.get_text())

import os
path="C:/Users/DE/Documents/__MACOSX"
import pandas as pd
from pandas import ExcelWriter
filepaths=[]
for file in os.listdir(path):
    if file.endswith('.csv'):
        filepath=path+'/'+file
        filepaths.append(filepath)
df=pd.read_csv(filepaths[0],index_col=0).set_index('ID')
text=2017
for i in range(1,len(filepaths)):
    df1=pd.read_csv(filepaths[i],index_col=0).set_index('ID')   
    text+=1
    df=df.join(df1, rsuffix=('_'+ str(text)))
with ExcelWriter('C:/Users/DE/Documents/datatonghop.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')
        
    

        

            
        

    

    
