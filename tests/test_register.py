from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register():
    driver = webdriver.Chrome()
    try:
        driver.get("file:///C:/Users/yory/Desktop/ALURA/inmersion-dev-aula2-proyecto-base/FORM/INDEXFORM.HTML")

       
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sign-up-btn"))
        )
       
        driver.save_screenshot("reports/screenshots/test_register.png")
    finally:
        driver.quit()
