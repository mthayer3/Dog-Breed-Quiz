import requests
import urllib.request
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


dog_list = [
"Affenpinscher",
"Afghan Hound",
"Airedale Terrier",
"Akita",
"Alaskan Klee Kai",
"Alaskan Malamute",
"American Bulldog",
"American English Coonhound",
"American Eskimo Dog",
"American Foxhound",
"American Hairless Territory",
"American Leopard Hound",
"American Staffordshire Terrier",
"American Water Spaniel",
"Anatolian Shepherd Dog",
"Appenzeller Sennenhund",
"Australian Cattle Dog",
"Australian Kelpie",
"Australian Shepherd",
"Australain Stumpy Tail Cattle Dog",
"Australian Terrier",
"Azawakh",
"Barbado de Terceira",
"Barbet",
"Basenji"
]

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.akc.org/dog-breeds/"
for i in range(len(dog_list)):
    dog_list[i] = dog_list[i].replace(" ", "-")
print(dog_list)


for i in dog_list:
    time.sleep(1)
    driver.get(url+i)

    

    # driver.get(url+"Affenpinscher")


# response = requests.get(url+ "Affenpinscher")
# print("Response: ", response.status_code, response.url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    score_list = soup.find_all("div", class_ = "breed-trait-score__score-wrap")
    coat_stats = soup.find_all("div", class_ = "breed-trait-score__choices" )
    list_of_scores = []



    coat_type = []
    coat_length = []
    coat_type = coat_stats[0].find_all("div", class_ = "breed-trait-score__choice--selected")
    coat_length = coat_stats[1].find_all("div", class_= "breed-trait-score__choice--selected")

    # Find coat type
    for i in range(len(coat_type)):
        coat_type[i] = coat_type[i].find("span").text.strip()
    print(coat_type)

    #Find coat length
    for i in range(len(coat_length)):
        coat_length[i] = coat_length[i].find("span").text.strip()


    print(coat_length)


    for i in range(14):
        score = []
        score = score_list[i].find_all("div", class_ = "breed-trait-score__score-unit breed-trait-score__score-unit--filled")
        list_of_scores.append(len(score))




    print(list_of_scores)
    with open('final.txt', 'a') as f:
        # f.write(list_of_scores)
        for i in range(len(list_of_scores)-1):
            f.write(str(list_of_scores[i])+",")
        f.write(str(list_of_scores[-1]))
        f.write("\n")

    # with open("scraping.txt","w", encoding = "utf-8") as variable_name:
    #     variable_name.write(soup.prettify())
    # print(soup.prettify())
driver.quit()




