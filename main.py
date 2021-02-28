from selenium import webdriver

chromeDriverPath = "../chromedriver"
driver = webdriver.Chrome(chromeDriverPath)


uri = "https://pvp.giustizia.it/pvp/"


driver.get(uri)

//driver.quit()