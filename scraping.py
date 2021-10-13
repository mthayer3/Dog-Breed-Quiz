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
driver.get(url+"Affenpinscher")
# response = requests.get(url+ "Affenpinscher")
# print("Response: ", response.status_code, response.url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

score_list = soup.find_all("div", class_ = "breed-trait-score__score-wrap")
list_of_scores = []

print(score_list[0])
print(len(score_list))

for i in range(14):
    score = []
    score = score_list[i].find_all("div", class_ = "breed-trait-score__score-unit breed-trait-score__score-unit--filled")
    list_of_scores.append(len(score))




print(list_of_scores)

# with open("scraping.txt","w", encoding = "utf-8") as variable_name:
#     variable_name.write(soup.prettify())
# print(soup.prettify())
driver.quit()




