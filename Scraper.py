import requests
from bs4 import BeautifulSoup
import datetime
import subprocess
import os


def CheckLog():
    ans = os.path.exists("log.txt")
    if ans is True:
        pass
    else:
        file_create = open("log.txt", "w+")
        file_create.close()


def NodeJS():
    URL = "https://nodejs.org/en/download/"

    page = requests.get(URL)
    # print("Respone code is:", page)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='main') # Finds the content wrapped inside the tag with id main
    
    # Finds the p tag with the class color-lightgray from the results obtained from above
    required_results = results.find_all('p', class_='color-lightgray')

    # print(required_results)

    for required in required_results:
        
        # Finds the strong tag
        version_name = required.find('strong') 
        if None in version_name:
            continue
        
        # Getting the text inside the strong tag
        print("Latest version of Node is:", version_name.text.strip()) 

        # Runs the node -v command and gets the printed version number 
        initial_version = str(subprocess.check_output(['node', '-v']).strip()).split("'")

        data = {"Date/Time": str(datetime.datetime.now()),
                "Version-fetched": version_name.text.strip(),
                "Initial-version": initial_version[1]}

        # Writing the dictionary data to the log.txt file in append mode
        with open("log.txt", "a") as write_file:
            write_file.write("\n")
            write_file.write(str(data))
        break


CheckLog()
NodeJS()
