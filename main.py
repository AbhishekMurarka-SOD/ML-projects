from selenium import webdriver
from save_images import make_directory,save_images
from scrap_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException

#Creating a instance of google Chrome
DRIVER_PATH='E:\\Assignment2\\chromedriver.exe'

# To run chrome in a headfull mode(like regular chrome)
driver= webdriver.Chrome(executable_path=DRIVER_PATH)
current_page_url=driver.get('https://www.amazon.in/s?k=saree+for+women+latest+design+2020&crid=3TN9I6RNKS7HS&sprefix=saree%2Caps%2C299&ref=nb_sb_ss_i_1_5')

DIRNAME="saree"
make_directory(DIRNAME)

start_pages= 1
total_pages= 5

for page in range(start_pages,  total_pages+1):
    try:
        product_details=scrap_image_url(driver=driver)
        print("scraping page {0} of {1} pages".format(page, total_pages))

        page_value=driver.find_element_by_xpath("//a[@class='a-pagination']").text
        print("The current page scraped is {}".format(page_vlaue))

        save_images(data=product_details, dirname=DIRNAME, page=page)
        print("Scraping of page {0} dobe".format(page))

        button_type=driver.find_element_by_xpath("//div[@class='a-disabled']//a[@class='a-last").get_attribute('innerHTML')

        if button_type == 'Next':
            driver.find_element_by_xpath("//a[@class='a-last']").click()
        else:
            driver.find_element_by_xpath("//a[@class='a-normal'][2]").click()

        new_page= driver.find_element_by_xpath("//a[@class='a-pagination']").text
        print("The new page is {}".format(new_page))

    except StaleElementReferenceException as Exception:

        Print("We are facing an exception")

        exp_page=driver.find_element_by_xpath("//a[@class='a-pagination']").text
        print("The Page Value at the time of exception is {}".format(exp_page))

        value=driver.find_element_by_xpath("//a[@class='a-pagination']")
        link=value.get_attribute('href')
        driver.get(link)

        product_details = scrap_image_url(driver=driver)
        print("scraping page {0} of {1} pages".format(page, total_pages))

        page_value = driver.find_element_by_xpath("//a[@class='a-pagination']").text
        print("The current page scraped is {}".format(page_vlaue))

        save_images(data=product_details, dirname=DIRNAME, page=page)
        print("Scraping of page {0} dobe".format(page))

        button_type = driver.find_element_by_xpath("//div[@class='a-disabled']//a[@class='a-last").get_attribute(
            'innerHTML')

        if button_type == 'Next':
            driver.find_element_by_xpath("//a[@class='a-last']").click()
        else:
            driver.find_element_by_xpath("//a[@class='a-normal'][2]").click()

        new_page = driver.find_element_by_xpath("//a[@class='a-pagination']").text
        print("The new page is {}".format(new_page))