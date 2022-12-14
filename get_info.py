import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GetInfoOf:
    def __init__(self,driver:webdriver.Chrome,link):
        self.link=link
        self.driver = driver
        self.driver.get(self.link)
            
    def getName(self):
        try:
            self.name=self.driver.find_element(By.TAG_NAME,'h1').text
            return self.name
        except:
            return None
   
    def getImageLink(self):
        try:
            img=self.driver.find_element(By.CSS_SELECTOR,'img[width="200"]')
            img=img.get_attribute('src')
            return img
        except : 
            return None 
    def getLocation(self):
        try:
            location=self.driver.find_element(By.CSS_SELECTOR,'span[class="text-body-small inline t-black--light break-words"]')
            return location.text
        except : 
            return None  
    
    def getCertificationsLink(self):
        try:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(1)
            
            sections=self.driver.find_elements(By.CSS_SELECTOR,'section[id^="ember"]')
            for section in sections:
                try:
                    title=section.find_element(By.TAG_NAME,'h2').text
                    if "Licences et certifications" not in str(title).strip():
                        raise Exception('title cherched not found') 
                except:
                    title=section.find_element(By.CSS_SELECTOR,'span[aria-hidden="true"]').text
                if "Licences et certifications" in str(title).strip():
                    footer=section.find_element(By.CLASS_NAME,"pvs-list__footer-wrapper")
                    link=footer.find_element(By.TAG_NAME,'a').get_attribute("href")
                    return link     
        except:
            return None
    
    def getCertifications(self):
        try:
            
            link=self.getCertificationsLink()
            if link!=None:
                self.driver.get(link)
                time.sleep(3)

            sections=self.driver.find_elements(By.CSS_SELECTOR,'section[id^="ember"]')
            sectionCherched=None
            for section in sections:
                try:
                    try:
                        title=section.find_element(By.TAG_NAME,'h2').text
                        if "Licences et certifications" not in str(title).strip():
                            raise Exception('title not found') 
                    except:
                        title=section.find_element(By.CSS_SELECTOR,'span[aria-hidden="true"]').text
                    if "Licences et certifications" in str(title).strip():
                        sectionCherched=section
                        break
                except:
                    pass
            
            self.certificationsInfo=[]
            li_tags=sectionCherched.find_elements(By.TAG_NAME,'li')
            for li_tag in li_tags:
                info=li_tag.find_elements(By.CSS_SELECTOR,'span[aria-hidden="true"]')
                info=[_.text for _ in info]
                if info:
                    self.certificationsInfo.append(info)

            return self.certificationsInfo
            
            
        except : 
            return None 
