import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("kitten")
elem.send_keys(Keys.RETURN)

##############스크롤 기능############
SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break

    last_height = new_height

######스크롤 기능 끝    ###################

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
cnt = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_elements_by_css_selector(".eHAdSb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(cnt)+".jpg")
        cnt += 1
    except:
        pass
driver.close()


####클래스 네임이 중복 되는 경우도 있기 때문에 우클릭 복사로 할것


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()