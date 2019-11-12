
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import string


recomendations = []
def top_five_suggestions(results):
    for recomendation in results:
        recomendations.append(recomendation.text)

url = "http://google.com"
driver = webdriver.Firefox()
driver.get(url)

for letter in string.ascii_lowercase[:3]:
    search_box = driver.find_element_by_xpath("//*[@title=\"Search\"]")
    search_box.clear();
    for char in f"digital nomad web developer {letter}":
        search_box.send_keys(char)

    results_box = driver.find_element_by_xpath("//*[@role=\"listbox\"]")
    time.sleep(2)
    results = results_box.find_elements_by_tag_name("span")
    top_five_suggestions(results)

# recomendations = ['how to be a digital nomad web developer', 'how to be a digital nomad web developer', 'certification', 'cover letter', 'career', 'course', 'certificate']



print(recomendations)


# driver.quit()
