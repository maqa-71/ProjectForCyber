from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def check_amazon_price():
    # Настройка браузера
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)


    driver.get("https://www.amazon.com/Smartphone-Unlocked-Processor-Manufacturer-Warranty/dp/B0DP3G4GVQ/ref=sr_1_5?crid=3DQ3DUU7PFLFU&dib=eyJ2IjoiMSJ9.9Ot5Yj2vovtORJgFfPO7Dij_EMtNIu46sOGx0ZMzrNP-_jlIp652r6pQf1E4WAUoXSfmEb7v1rLGZFFipKzMITpjJkB-uL4u5dbhghi5Xkiet0Qcd1PdzgzCiVKjf-7qc4fak9cn1SnuNl6szoQ4PUwMqg9ELJkrScHflFt6AewXPDUEu_fivAoAl0eaPQORG6Nduxz4qp2EAZaX-W4eEDlBRw8un2z9CivXObvkJHo.cc95rxqVYB56_hia6O-cr3NeiRlkMPQc1b5jHSzdWCc&dib_tag=se&keywords=iphone%2B17&qid=1763019662&sprefix=iphon%2Caps%2C245&sr=8-5&th=1")  

    try:
        # Ждём появления элемента с классом 'a-price-whole'
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
        )

        # Получаем текст цены
        price = price_element.text
        print(f" Текущая цена товара: {price}")

    except Exception as e:
        print(" Ошибка при получении цены:", e)

    finally:
        time.sleep(3)
        driver.quit()

check_amazon_price()
