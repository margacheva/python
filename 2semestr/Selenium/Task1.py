"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
Beautiful Soup — это библиотека Python для извлечения данных из файлов HTML и XML.
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# создаем объект опций для драйвера Chrome
options = Options()

# создаем объект драйвера Chrome
driver = webdriver.Chrome(options=options)

# переходим на страницу магазина Steam
driver.get("https://store.steampowered.com/")

# находим поле поиска и вводим запрос "Стратегии"
search = driver.find_element(By.XPATH, "//*[@id=\"store_nav_search_term\"]")
search.send_keys("Стратегии")
search.send_keys(Keys.ENTER)

# получаем исходный код страницы и создаем объект BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, "lxml")

# находим все элементы с названиями игр
name = soup.find_all("div", "responsive_search_name_combined")

# выводим названия игр в консоль
k = 1
for i in name:
    title = i.find("span", "title").text
    print(f"{k} место: {title}")
    k += 1 # увеличиваем счетчик места на 1 после каждой итерации цикла)
print("done")