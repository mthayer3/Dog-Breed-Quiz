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
"American Hairless Terrier",
"American Leopard Hound",
"American Staffordshire Terrier",
"American Water Spaniel",
"Anatolian Shepherd Dog",
"Appenzeller Sennenhund",
"Australian Cattle Dog",
"Australian Kelpie",
"Australian Shepherd",
"Australian Stumpy Tail Cattle Dog",
"Australian Terrier",
"Azawakh",
"Barbado da Terceira",
"Barbet",
"Basenji",
"Basset Fauve de Bretagne",
"Basset Hound",
"Bavarian Mountain Scent Hound",
"Beagle",
"Bearded Collie",
"Beauceron",
"Bedlington Terrier",
"Belgian Laekenois",
"Belgian Malinois",
"Belgian Sheepdog",
"Belgian Tervuren",
"Bergamasco Sheepdog",
"Berger Picard",
"Bernese Mountain Dog",
"Bichon Frise",
"Biewer Terrier",
"Black and Tan Coonhound",
"Black Russian Terrier",
"Bloodhound",
"Bluetick Coonhound",
"Boerboel",
"Bohemian Shepherd",
"Bolognese",
"Border Collie",
"Border Terrier",
"Borzoi",
"Boston Terrier",
"Bouvier des Flandres",
"Boxer",
"Boykin Spaniel",
"Bracco Italiano",
"Braque du Bourbonnais",
"Braque Francais Pyrenean",
"Briard",
"Brittany",
"Broholmer",
"Brussels Griffon",
"Bull Terrier",
"Bulldog",
"Bullmastiff",
"Cairn Terrier",
"Canaan Dog",
"Cane Corso",
"Cardigan Welsh Corgi",
"Carolina Dog",
"Catahoula Leopard Dog",
"Caucasian Shepherd Dog",
"Cavalier King Charles Spaniel",
"Central Asian Shepherd Dog",
"Cesky Terrier",
"Chesapeake Bay Retriever",
"Chihuahua",
"Chinese Crested",
"Chinese Shar-Pei",
"Chinook",
"Chow Chow",
"Cirneco dellEtna",
"Clumber Spaniel",
"Cocker Spaniel",
"Collie",
"Coton de Tulear",
"Croatian Sheepdog",
"Curly-Coated Retriever",
"Czechoslovakian Vlcak",
"Dachshund",
"Dalmatian",
"Dandie Dinmont Terrier",
"Danish-Swedish Farmdog",
"Deutscher Wachtelhund",
"Doberman Pinscher",
"Dogo Argentino",
"Dogue de Bordeaux",
"Drentsche Patrijshond",
"Drever",
"Dutch Shepherd",
"English Cocker Spaniel",
"English Foxhound",
"English Setter",
"English Springer Spaniel",
"English Toy Spaniel",
"Entlebucher Mountain Dog",
"Estrela Mountain Dog",
"Eurasier",
"Field Spaniel",
"Finnish Lapphund",
"Finnish Spitz",
"Flat-Coated Retriever",
"French Bulldog",
"French Spaniel",
"German Longhaired Pointer",
"German Pinscher",
"German Shepherd Dog",
"German Shorthaired Pointer",
"German Spitz",
"German Wirehaired Pointer",
"Giant Schnauzer",
"Glen of Imaal Terrier",
"Golden Retriever",
"Gordon Setter",
"Grand Basset Griffon Vendeen",
"Great Dane",
"Great Pyrenees",
"Greater Swiss Mountain Dog",
"Greyhound",
"Hamiltonstovare",
"Hanoverian Scenthound",
"Harrier",
"Havanese",
"Hokkaido",
"Hovawart",
"Ibizan Hound",
"Icelandic Sheepdog",
"Irish Red and White Setter",
"Irish Setter",
"Irish Terrier",
"Irish Water Spaniel",
"Irish Wolfhound",
"Italian Greyhound",
"Jagdterrier",
"Japanese Akitainu",
"Japanese Chin",
"Japanese Spitz",
"Japanese Terrier",
"Jindo",
"Kai Ken",
"Karelian Bear Dog",
"Keeshond",
"Kerry Blue Terrier",
"Kishu Ken",
"Komondor",
"Kromfohrlander",
"Kuvasz",
"Labrador Retriever",
"Lagotto Romagnolo",
"Lakeland Terrier",
"Lancashire Heeler",
"Lapponian Herder",
"Leonberger",
"Lhasa Apso",
"Lowchen",
"Maltese",
"Manchester Terrier Standard",
"Manchester Terrier Toy",
"Mastiff",
"Miniature American Shepherd",
"Miniature Bull Terrier",
"Miniature Pinscher",
"Miniature Schnauzer",
"Mountain Cur",
"Mudi",
"Neapolitan Mastiff",
"Nederlandse Kooikerhondje",
"Newfoundland",
"Norfolk Terrier",
"Norrbottenspets",
"Norwegian Buhund",
"Norwegian Elkhound",
"Norwegian Lundehund",
"Norwich Terrier",
"Nova Scotia Duck Tolling Retriever",
"Old English Sheepdog",
"Otterhound",
"Papillon",
"Parson Russell Terrier",
"Pekingese",
"Pembroke Welsh Corgi",
"Perro de Presa Canario",
"Peruvian Inca Orchid",
"Petit Basset Griffon Vendeen",
"Pharaoh Hound",
"Plott Hound",
"Pointer",
"Polish Lowland Sheepdog",
"Pomeranian",
"Poodle Miniature",
"Poodle Standard",
"Poodle Toy",
"Porcelaine",
"Portuguese Podengo",
"Portuguese Podengo Pequeno",
"Portuguese Pointer",
"Portuguese Sheepdog",
"Portuguese Water Dog",
"Pudelpointer",
"Pug",
"Puli",
"Pumi",
"Pyrenean Mastiff",
"Pyrenean Shepherd",
"Rafeiro do Alentejo",
"Rat Terrier",
"Redbone Coonhound",
"Rhodesian Ridgeback",
"Romanian Mioritic Shepherd Dog",
"Rottweiler",
"Russell Terrier",
"Russian Toy",
"Russian Tsvetnaya Bolonka",
"Saint Bernard",
"Saluki",
"Samoyed",
"Schapendoes",
"Schipperke",
"Scottish Deerhound",
"Scottish Terrier",
"Sealyham Terrier",
"Segugio Italiano",
"Shetland Sheepdog",
"Shiba Inu",
"Shih Tzu",
"Shikoku",
"Siberian Husky",
"Silky Terrier",
"Skye Terrier",
"Sloughi",
"Slovakian Wirehaired Pointer",
"Slovensky Cuvac",
"Slovensky Kopov",
"Small Munsterlander",
"Smooth Fox Terrier",
"Soft Coated Wheaten Terrier",
"Spanish Mastiff",
"Spanish Water Dog",
"Spinone Italiano",
"Stabyhoun",
"Staffordshire Bull Terrier",
"Standard Schnauzer",
"Sussex Spaniel",
"Swedish Lapphund",
"Swedish Vallhund",
"Taiwan Dog",
"Teddy Roosevelt Terrier",
"Thai Ridgeback",
"Tibetan Mastiff",
"Tibetan Spaniel",
"Tibetan Terrier",
"Tornjak",
"Tosa",
"Toy Fox Terrier",
"Transylvanian Hound",
"Treeing Tennessee Brindle",
"Treeing Walker Coonhound",
"Vizsla",
"Volpino Italiano",
"Weimaraner",
"Welsh Springer Spaniel",
"Welsh Terrier",
"West Highland White Terrier",
"Wetterhoun",
"Whippet",
"Wire Fox Terrier",
"Wirehaired Pointing Griffon",
"Wirehaired Vizsla",
"Working Kelpie",
"Xoloitzcuintli",
"Yakutian Laika",
"Yorkshire Terrier",
]

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.akc.org/dog-breeds/"
for i in range(len(dog_list)):
    dog_list[i] = dog_list[i].replace(" ", "-")

print(dog_list)


for dog in dog_list:
    time.sleep(2)
    driver.get(url+dog)

    

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
    with open('final.csv', 'a') as f:
        # f.write(list_of_scores)
        f.write(dog+",")
        for i in range(len(list_of_scores)):
            f.write(str(list_of_scores[i])+",")
        # f.write(str(list_of_scores[-1]))
        for i in coat_type:
            f.write(str(i)+" ")
        f.write(",")
        for i in coat_length:
            f.write(str(i)+" ")
        
        f.write("\n")

    # with open("scraping.txt","w", encoding = "utf-8") as variable_name:
    #     variable_name.write(soup.prettify())
    # print(soup.prettify())
driver.quit()




