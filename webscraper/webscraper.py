import requests
from bs4 import BeautifulSoup
import csv

#url of the website
url = "https://www.bbc.com/news"

#send a request to fetch the webpage content
response = requests.get(url)

#check the request is success
if response.status_code == 200:
    #parse the HTML content using beautifulsoup
    soup = BeautifulSoup(response.text, "html.parser")

    #find all new headlines
    headlines = soup.find_all("h2")  #BBC news having h3 tags


    # printing head lines
    print("Latest head lines :")

    #save all headlines
    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Index', 'HeadLines'])
        for index, headlines in enumerate(headlines, start=1):  #enumerate some kind of loop->iteration
            writer.writerow([index, headlines.text.strip()])
            print(f'{index}. {headlines.text.strip()}')
    print("HeadLines saved Successfully")


else:
    print(f'Failed to fetch webPage. Status code: {response.status_code}')
