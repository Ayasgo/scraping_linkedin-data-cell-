from get_alumni_links import *
from get_info import GetInfoOf
from time import sleep
import csv


NOMBRE_ALUMNI=30
driver=init()
connecting(driver)
sleep(2)
urlsAlumni=getAlumniLinks(driver=driver,nbrAlumni=NOMBRE_ALUMNI)
alumniInfo=[]

for i,url in enumerate(urlsAlumni):
    driver.execute_script("window.open('https://www.google.com/?hl=fr')")
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)

    alumnus=GetInfoOf(driver=driver,link=url)
    alumnusInfo=dict()
    sleep(1)
    alumnusInfo['name']=alumnus.getName()
    alumnusInfo['link']=alumnus.link
    alumnusInfo['img']=alumnus.getImageLink()
    alumnusInfo['location']=alumnus.getLocation()
    alumnusInfo['certifications']=alumnus.getCertifications()
    alumniInfo.append(alumnusInfo)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
successPercentage=len(alumniInfo)/len(urlsAlumni)
print(successPercentage)

with open('alumniInfo_.csv','w') as file:
    csv_writer = csv.writer(file)
    row=['name','link','img','location','Licences et certifications']
    csv_writer.writerow(row)

    for alumnus in alumniInfo:
        try:
            row=[alumnus['name'],alumnus['link'],alumnus['img'],alumnus['location'],alumnus['certifications']]
            csv_writer.writerow(row)
        except:
            pass

