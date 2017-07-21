# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:30:28 2017
@author: LuisMDlab
"""

""" Scrape Multiplus Facebook ID from .csv file Script"""

import time
import datetime
import csv
from selenium import webdriver #Importante module.

identify = []
link = []
cont = 0

# Open .csv file
arquivoExemplo = open('ID_find.csv')
leitorArquivo = csv.reader(arquivoExemplo)

#Add csv file into a list.
for row in leitorArquivo:
    link.append(row[0]) 
    
#Driver Start
browser = webdriver.Firefox()

#Time Monitor
print('Iniciando em: ' + str(datetime.datetime.now()))

#Start scrapping.
try:
    for i in link:
        browser.set_page_load_timeout(30)
        browser.get('https://findmyfbid.com/') #Site where Facebook links will be inputed
        inserirElem = browser.find_element_by_name('url') #Name of form element.
        inserirElem.send_keys(i) #Send links to form.
        inserirElem.submit() 
        
        # Idnetify Facebook ID on URL.
        while browser.current_url == 'https://findmyfbid.com/':
            print('.', end = '.')
        identify.append(browser.current_url) #Insert ULRs with the ID on a list.
        time.sleep(5)
        cont +=1
        if cont%50==0:
            print(str(cont) + ' IDs recuperados em ' + str(datetime.datetime.now()))
        
    browser.quit()
    
    
    outputFile = open('saveID', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    for row in identify:
        outputWriter.writerow(row)
    outputFile.close()
    
    print(str(cont) + ' IDs recuperados em ' + str(datetime.datetime.now()))
    
#Save IDs in case of fail.
except Exception as e:
    print(e)
    outputFile = open('saveID', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    for row in identify:
        outputWriter.writerow(row)
    outputFile.close() 
    print('Got an error but: '+ str(cont) + ' IDs recovered in ' + str(datetime.datetime.now()))
    
#It's necessary download geckodriver and add it to PATH. https://github.com/mozilla/geckodriver/releases
