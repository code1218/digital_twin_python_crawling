from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://naver.com")
    driver.maximize_window()
    sleep(0.5)

    webtoonHomeLink = driver.find_element(
        by=By.CSS_SELECTOR,
        value="#shortcutArea > ul > li:nth-child(9) > a")
    webtoonHomeUrl = webtoonHomeLink.get_attribute("href")
    driver.get(webtoonHomeUrl)
    sleep(0.5)
    print(driver.current_url)

    webtoonLink = driver.find_element(
        by=By.CSS_SELECTOR,
        value="#menu > li:nth-child(2) > a")
    webtoonLink.click()
    sleep(0.5)
    print(driver.current_url)

    dayOfWeeks = driver.find_elements(
        by=By.CSS_SELECTOR,
        value="#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a")

    webtoonList = []

    for dayOfWeek in dayOfWeeks[1:3]:
        dayOfWeek.click()
        sleep(0.5)

        webtoonDict = {
            "dayOfWeek": dayOfWeek.text,
            "webtoonItems": []
        }

        webtoonItems = driver.find_elements(
            by=By.CSS_SELECTOR,
            value="#content > div:nth-child(1) > ul > li")

        for webtoonItem in webtoonItems:
            driver.execute_script("arguments[0].scrollIntoView(true)", webtoonItem)
            webtoonItemImg = webtoonItem.find_element(by=By.CSS_SELECTOR, value="a > div > img")
            webtoonItemImgSrc = webtoonItemImg.get_attribute("src")
            print(webtoonItemImgSrc)
            webtoonItemTitle = webtoonItem.find_element(
                by=By.CSS_SELECTOR,
                value="div > a:nth-of-type(1) > span")
            webtoonItemTitleText = webtoonItemTitle.text
            print(webtoonItemTitleText)
            webtoonItemAuthor = webtoonItem.find_element(
                by=By.CSS_SELECTOR,
                value="div .ContentAuthor__author--CTAAP")
            webtoonItemAuthorText = webtoonItemAuthor.text
            print(webtoonItemAuthorText)
            webtoonItemRating = webtoonItem.find_element(
                by=By.CSS_SELECTOR,
                value="div > div:nth-last-of-type(1) > span > span")
            webtoonItemRatingText = webtoonItemRating.text
            print(webtoonItemRatingText)

            webtoonItemDict = {
                "img": webtoonItemImgSrc,
                "title": webtoonItemTitleText,
                "author": webtoonItemAuthorText,
                "rating": webtoonItemRatingText
            }

            webtoonDict["webtoonItems"].append(webtoonItemDict)

            sleep(0.1)

        webtoonList.append(webtoonDict)
    print(webtoonList)









