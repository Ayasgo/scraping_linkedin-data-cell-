import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



LINKEDIN_CONNECTING_LINK = "https://www.linkedin.com/login/fr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
LINK_ALUMNI="https://www.linkedin.com/school/institut-national-des-postes-et-telecommunications/people/?educationEndYear=2019&educationStartYear=2000&facetGeoRegion=102787409"

def init():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--disable-default-apps")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
    return driver


def connecting(driver):
    driver.get(LINKEDIN_CONNECTING_LINK)

    email=os.environ.get('email')
    linkdenPassword=os.environ.get('Linkden')

    username=driver.find_element(By.ID,"username")
    username.send_keys(email)
    password=driver.find_element(By.ID,"password")
    password.send_keys(linkdenPassword)

    time.sleep(1)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/form[1]/div[3]/button[1]").send_keys(Keys.ENTER)


def getAlumniLinks(driver,nbrAlumni):
    urlsAlumni=[]
    driver.get(LINK_ALUMNI)
    height=0
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,2000);")
    for i in range(1,nbrAlumni+1):
        pasOfHeight=random.randrange(360,500)  #en px
        height+=pasOfHeight
        driver.execute_script(f"window.scrollTo(0,{height});")
        time.sleep(2)
        element=f"//body/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[{i}]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/a[1]"
        url=driver.find_element(By.XPATH,element).get_attribute("href")
        urlsAlumni.append(url)

    return urlsAlumni

