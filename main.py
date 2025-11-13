from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def check_amazon_price():
    # Настройки браузера
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Автоматическая установка подходящего ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Пример товара (можно заменить на любой URL)
    url = "https://www.amazon.com/Apple-Generation-Cancelling-Transparency-Personalized/dp/B0CHWRXH8B/ref=sr_1_1?crid=1AB3GQU3QX3U5&dib=eyJ2IjoiMSJ9.sxiu6THrWjTusdewg6PRCwsCOH3UrKmr-9PG_Iocu5yaezj2x-Svqpf1obqlygmpGFIVS0WYRazH5n19qS7qe7rFt6QhBCO1WjeoL3ccKPKST9bHHqjDMRx6MhJLZM7HdGOT1OPBeoMY0uzEjO3QfYQO3kbT8FJhOLcQ8LVDq6Y7Df7WC0jwRe177PwowfSxcllmH9Qw8BPeDIehxVYzVjcvzeo8VRFLev2nOVIctmI.mUXybttsEj4Tr2MJQFvpsDcxW2Zyfr0J_lY0OdQgw1o&dib_tag=se&keywords=airpods+pro&qid=1763016602&sprefix=airpods%2Caps%2C255&sr=8-1"  
    driver.get(url)

    try:
        # Ожидаем появления цены (Amazon может использовать разные классы)
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='a-price-whole' or @id='priceblock_ourprice' or @id='priceblock_dealprice']")
            )
        )

        price = price_element.text
        print(f"💲 Текущая цена товара: {price}")

    except Exception as e:
        print("⚠ Ошибка при получении цены:", e)

    finally:
        time.sleep(3)
        driver.quit()

# Запуск функции
check_amazon_price()
