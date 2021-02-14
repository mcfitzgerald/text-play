import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set up driver options
options = Options()
options.add_argument("--headless")


def scroll(driver, timeout):
    flag = 1

    # Get current scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while flag == 1:

        # Scroll to bottom and wait to load
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("scrolling...")
        time.sleep(timeout)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            print("end of page reached")
            flag = 0

        last_height = new_height


def get_source(url, timeout=5):
    # set up driver
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    scroll(driver, timeout)

    source = driver.page_source

    driver.close()

    return source
