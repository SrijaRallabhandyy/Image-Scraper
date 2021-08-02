#All the necessary imports

from selenium import webdriver
import time
import re
import requests
import os
import urllib.request

#Set of inputs
path="E:/Accenture/Image_Classifier/" # Path for the folder where the images must be scraped to
folder_name="Myntra" #Folder name which needs to be changed along with URL
url="https://www.myntra.com/" #URL of the E-Commerce website

DRIVER_PATH = 'C:/chromedriver_win32/chromedriver.exe' # Path to the chrome driver
#Code to open the website and scroll till bottom to make sure the webpage loads till the end
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
count=0
y = 1000
for timer in range(0,50):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 100
    time.sleep(1)
time.sleep(10)
page_source=driver.page_source
print(page_source)
all_double_quotes=(re.findall('"([^"]*)"', page_source))


image_urls=[] #List of all the image URLs in the given webpage
#Function to download the images into the given folder
def download_images(image_link,path):
    count=0
    for i in image_link:
        try:
            count = count + 1
            i=i.replace(" ","%20")
            # print(i)
            urllib.request.urlretrieve(i, path+"/"+str(count)+".jpg")
            print(path+"/"+str(count)+".jpg")
        except:
            pass

#Creating a folder
def folder_create(folder_name):
    try:
        os.mkdir(folder_name)
    # if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name!")
        folder_create()
folder_create(folder_name)

#Parsing the html string to get all the urls of the images(.jpg)
for i in all_double_quotes:
    if i.find(".jpg") !=-1:
        image_urls.append(i)
        # print(i)
        # print("\n")
    else:
        continue
final_urls=[]

# String parsing to remove some errors like adding https:// to the image URL(If not present)
for j in image_urls:
    image_link = j.replace("{width}", "500")
    if (image_link.startswith('http:') or image_link.startswith('https:')):
        pass
    else:
        image_link = "https:" + image_link
    final_urls.append(image_link)

final_urls=list(set(final_urls))
download_images(final_urls, path + folder_name)

for i in final_urls:
    print(i)




