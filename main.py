from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_button_with_role(url):
    # Настраиваем браузер
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service()

    # Запуск Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    try:
        # Ждём появления кнопки с role="button"
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='button']"))
        )

        # Кликаем по кнопке
        button.click()
        print("✅ Кнопка успешно найдена и нажата!")

    except Exception as e:
        print("⚠ Ошибка:", e)

    finally:
        time.sleep(3)
        driver.quit()

# Пример вызова (замени URL на страницу, где есть кнопка)
click_button_with_role("https://www.amazon.com")
