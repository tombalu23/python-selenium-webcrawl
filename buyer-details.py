import selenium
from selenium import webdriver


#Create and open csv file to store data
filename='buyer-price.csv'
f=open(filename, 'w')
headers='Buyer Name,Price \n'
f.write(headers)



MAX_PAGE=5       #No. of pages
page_no=1
url='http://econpy.pythonanywhere.com/ex/001.html'
browser= webdriver.Chrome()               #open Google Chrome browser


#To scrape pages from 1 to 5
for page_no in range(1 , MAX_PAGE+1):
    url=url[:38]+str(page_no)+url[39:]
    browser.get(url)


    #Extract values of buyers and prices
    buyers=browser.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices=browser.find_elements_by_xpath('//span[@class="item-price"]')

    num_page_items=len(buyers)

    #Write data to csv
    for i in range (num_page_items):
        print(buyers[i].text+','+prices[i].text)
        f.write(buyers[i].text + ',' + prices[i].text + '\n')

f.close()





