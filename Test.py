from selenium import webdriver

browser = webdriver.Chrome('/Users/sharan_sreesai/Documents/try-selenium/chromedriver')
browser.get('https://selenium.dev/')
elem = browser.find_element_by_link_text('Downloads')
elem.get_attribute('href')
elem.click()