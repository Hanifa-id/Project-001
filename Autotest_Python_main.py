import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
s=Service('D:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Заполнение формы Паспорт
driver.get("https://qa.neapro.site/login") # Открытие сайта
driver.maximize_window() # Окно на весь экран
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("test@gmail.com") # Email
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("12345678") # Пароль
driver.find_element(By.XPATH, "//button[@type='submit']").click() # Подтвердить
time.sleep(3)
driver.find_element(By.XPATH, "//div[2]/div[2]/div").click() # Открытие формы паспорта
driver.find_element(By.ID, "surname").send_keys(Keys.HOME, "Петров") # Фамилия
driver.find_element(By.ID, "name").send_keys(Keys.HOME, "Петр") # Имя
driver.find_element(By.ID, "patronymic").send_keys(Keys.HOME, "Петрович") # Отчество
driver.find_element(By.XPATH, "//*[@id='birthday']/div/input").send_keys(Keys.HOME, "01.01.1999") # Дата рождения
driver.find_element(By.ID, "passportSeries").send_keys(Keys.HOME, "1234") # Паспорт серия
driver.find_element(By.ID, "passportNumber").send_keys(Keys.HOME, "123456") # Паспорт номер
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").send_keys(Keys.HOME, "20.02.2002") # Дата выдачи
driver.find_element(By.ID, "code").send_keys(Keys.HOME, "654321") # Код подразделения
driver.find_element(By.ID, "cardId").send_keys(Keys.HOME, "12345678901") # СНИЛС
driver.find_element(By.ID, "issued").send_keys(Keys.HOME, "Паспортный отдел") # Кем выдан
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.HOME, "г Москва ул Магаданская") # Адрес
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.DOWN, Keys.RETURN) # Выбор из дадаты
driver.find_element(By.ID, "phone").send_keys(Keys.PAGE_DOWN, Keys.HOME, "9876543210") # Телефон
driver.find_element(By.XPATH, "//input[@type='file']").send_keys("D:/Desktop/kubik.jpg") # Прикрепить
driver.find_element(By.XPATH, "//button[2]").click() # Отправить

# Подтверждение паспорта
driver.get("https://adminqa.neapro.site/login") # Открытие админки
driver.find_element(By.ID, 'admin_email').send_keys('test@neapro.ru') # Email
driver.find_element(By.ID, 'admin_password').send_keys('12345678') # Пароль
driver.find_element(By.NAME, 'commit').click() # Войти
driver.get("https://adminqa.neapro.site/documents?q%5Buser_id_eq%5D=2014") # Открытие страницы пользователя
driver.find_element(By.XPATH, "/html//table[@id='index_table_documents']/tbody/tr[1]//div[@class='tag-select-container']/div[1]").click() # Статус Ожидание
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys('Принят', Keys.ENTER) # Статус Принят
time.sleep(2)

# Смена номера телефона и выход из ЛК
driver.get("https://qa.neapro.site/login") # Открытие сайта
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("test@gmail.com") # Email
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("12345678") # Пароль
driver.find_element(By.XPATH, "//button[@type='submit']").click() # Подтвердить
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[2]/a").click() # Профиль
driver.find_element(By.XPATH, "//div[@id='__layout']//div[@class='main']/div//ul//a[@href='/cabinet/security']").click() # Безопасность
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]").click() # Изменить телефон
driver.find_element(By.XPATH, "//input[@type='text']").clear() # Очистка
driver.find_element(By.XPATH, "//input[@type='text']").send_keys(Keys.HOME, "1111111111") # Новый номер
driver.find_element(By.XPATH, "//button[@type='submit']").click() # Подтвердить
driver.find_element(By.XPATH, ".//*[@id='__layout']/div/div[1]/div/div[2]").click() # Боковая панель
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[1]/div/div").click() # Выйти