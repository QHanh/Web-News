from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.os_manager import ChromeType
from time import sleep

def get_news_info(news_elm, driver1):
    title = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').text
    url = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').get_attribute('href')
    driver1.get(url)
    sleep(2)
    time_str = driver1.find_element(By.ID, 'hidLastModifiedDate').get_attribute('value')
    count_like = 0
    try:
        iframes = driver1.find_elements(By.TAG_NAME, 'iframe')
        for iframe in iframes:
            driver1.switch_to.frame(iframe)
            try:
                count_like = driver1.find_element(By.CLASS_NAME, '_5n6h').text
                count_like = count_like.replace(',', '')
                if 'K' in count_like:
                    count_like = float(count_like.replace('K', '')) * 100
                count_like = int(count_like)
                break
            except NoSuchElementException:
                driver1.switch_to.default_content()
                continue
    except (IndexError, NoSuchElementException):
        count_like = 0

    result = {
        'Title': title,
        'Url': url,
        'Like': count_like,
        'Time': time_str
    }
    return result

def scrape():
    url = 'https://cafebiz.vn'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver1 = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    driver.get(url)
    list_news_pos = driver.find_element(By.CLASS_NAME, 'cfbiz_home20-wrapper')
    news_list = list_news_pos.find_elements(By.CLASS_NAME, 'cfbiznews_box')

    all_product_list = []

    for new_elm in news_list[:6]:
        news_info = get_news_info(news_elm=new_elm, driver1=driver1)
        all_product_list.append(news_info)

    driver.quit()
    driver1.quit()

    return all_product_list
