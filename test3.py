from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

controlador = webdriver.Chrome(executable_path= "C:\Program Files\driver\chromedriver.exe")
controlador.get ("https://lavandanatural.com")
controlador.maximize_window()
time.sleep(3)

contact = controlador.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/ul/li[3]/a")
contact.click()
time.sleep(3)

insta = controlador.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[2]/div/div[1]/div/ul[2]/li[1]/a")
insta.click()
time.sleep(7)



requirement = ()  #Expected Result
labelObtained = ()  #Actual Result

def compareLabels():
    if requirement in labelObtained:
        print ("Pass")
    else:
        print ("Fail")


campoContacto = controlador.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/ul/li[3]/a")

labelCampoContacto = controlador.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/ul/li[3]/a").text

labelObtained =labelCampoContacto
print(labelObtained)

requirement = 'CONTACTO'

compareLabels()



controlador.close()