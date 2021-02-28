from selenium import webdriver
import time

chromeDriverPath = "../chromedriver"
driver = webdriver.Chrome(chromeDriverPath)


uri = "https://pvp.giustizia.it/pvp/"
address = "Bergamo, Province of Bergamo, Italy"

driver.get(uri)

modalBtn = driver.find_element_by_class_name("bottoni-chiusura")
modalBtn.click()

time.sleep(5)

driver.quit()