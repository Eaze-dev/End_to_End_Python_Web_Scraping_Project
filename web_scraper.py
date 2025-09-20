"""
give the url
file name
greetings
start scraping
hotel_name
price
location
ratings
reviews
link
save the file

"""

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random

#url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=Johannesburg&ssne=Johannesburg&ssne_untouched=Johannesburg&label=gen173nr-10CAEoggI46AdIM1gEaPsBiAEBmAEzuAEXyAEM2AED6AEB-AEBiAIBqAIBuAKszrrGBsACAdICJDk3M2ZmYWI5LWU3M2YtNGZlYS05N2ZkLWMwMTg0ZmQ4Yjc4NNgCAeACAQ&sid=84d923c6d6259adb595ed3873b90be62&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-1240261&dest_type=city&checkin=2025-10-01&checkout=2025-10-02&group_adults=2&no_rooms=1&group_children=0'
#cape_town = 'https://www.booking.com/searchresults.en-gb.html?ss=Cape+Town&ssne=Cape+Town&ssne_untouched=Cape+Town&label=gen173nr-10CAEoggI46AdIM1gEaPsBiAEBmAEzuAEXyAEM2AED6AEB-AEBiAIBqAIBuAKszrrGBsACAdICJDk3M2ZmYWI5LWU3M2YtNGZlYS05N2ZkLWMwMTg0ZmQ4Yjc4NNgCAeACAQ&sid=84d923c6d6259adb595ed3873b90be62&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-1217214&dest_type=city&checkin=2025-10-01&checkout=2025-10-02&group_adults=2&no_rooms=1&group_children=0'

def web_scraper2(web_url, file_name):

    #Welcome message
    print("Thank you for sharing the url and file name!\nReading the content")

    #Processsing
    num = random.randint(3, 5)
    time.sleep(num)


    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}


    response = requests.get(web_url, headers=header)

    if response.status_code == 200:
        print("Connected to the website")
        html_content = response.text

        #Create soup
        soup = BeautifulSoup(html_content, 'lxml')

        #Main Containers
        hotel_divs = soup.find_all('div', role="listitem")

        with open(f'{fn}.csv', 'w', newline='', encoding='utf-8-sig') as file_csv:
            writer = csv.writer(file_csv)

            #Adding header
            writer.writerow(['hotel_name', 'locality', 'price', 'rating', 'score', 'review', 'link'])

            for hotel in hotel_divs:
                hotel_name = hotel.find('div', class_="b87c397a13 a3e0b4ffd1").text.strip()
                hotel_name if hotel_name else "NA"

                #location
                location = hotel.find('span', class_="d823fbbeed f9b3563dd4").text.strip()
                location if location else "NA"

                #price
                price = hotel.find('span', class_="b87c397a13 f2f358d1de ab607752a2").text.replace('ZAR', '').strip()
                price if price else "NA"

                #Rating
                rating = hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63").text.strip()
                rating if rating else "NA"

                #Score
                score = hotel.find('div', class_="f63b14ab7a dff2e52086").text.strip()
                score if score else "NA"

                #Reviews
                review = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
                review if review else "NA"

                #Getting the link
                link = hotel.find('a', href=True).get('href')
                link if link else "NA"

                #Saving the file into csv
                writer.writerow([hotel_name, location, price, rating, score, review, link])
                
        print('Web scraping done!')


    else:
        print(f"Connection failed!{response.status_code}")

if __name__ == '__main__':

    url = input("Please enter url!: ")
    fn = input("Please provide the file name: ")

    #Calling the Function
    web_scraper2(url, fn)








