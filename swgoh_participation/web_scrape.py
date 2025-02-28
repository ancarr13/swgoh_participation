#File to scrape swgoh.gg for guild info
#Author: Anthony Carroll, gitlab: ancarr13, email: anthonymcarrol13@gmail.com
#Date created: 9/17/2024

#Import necessary packages
import requests
from bs4 import BeautifulSoup


#scraping function

def scrape():

    url = 'https://swgoh.gg/g/wwN9448kSiWStXSSm5NblQ/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #debug
    out = open("out.txt", "w+")
    out.write(str(soup))
    out.close

    

if __name__ == '__main__':
    scrape()
