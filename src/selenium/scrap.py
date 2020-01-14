# perso
import src.utils as ut
from selenium import webdriver

# system
import sys
import json 

# external
import scrapy
import csv

MAX_PAGE = 5
MAX_DIGIT = 3

def get_page_id(i):
    page_id = ""
    for _ in range(MAX_DIGIT - len(str(i))):
        page_id += "0"
    page_id += str(i)
    return page_id 

def main():
    args = sys.argv
    project_params = json.load(open(args[1]))
    scrap_params = json.load(open(args[2]))

    with open("data/test.csv", "w") as csv_urls:
        csv_urls = csv.writer(csv_urls)
        # open firefox
        driver = webdriver.Firefox()

        for i in range(MAX_PAGE):
            page_id = get_page_id(i)
            print(page_id)
            driver.get('http://econpy.pythonanywhere.com/ex/{}.html'.format(page_id))

        # /html/body/div[2]/div

            buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
            prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
        

            for buyer, price in zip(buyers,prices):
                csv_urls.writerow([buyer.text, price.text])
        

    driver.close()


if __name__ == "__main__":
    main()