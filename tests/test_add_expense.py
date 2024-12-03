from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_expense():
    driver = webdriver.Chrome()
    try:
        driver.get("file:///C:/Users/yory/Desktop/ALURA/inmersion-dev-aula2-proyecto-base/index.html")
        driver.find_element(By.ID, "nombreGasto").send_keys("Comida")
        driver.find_element(By.ID, "valorGasto").send_keys("250.50")
        driver.find_element(By.ID, "botonFormulario").click()
        driver.save_screenshot("reports/screenshots/test_add_expense.png")
        assert "Comida" in driver.page_source
        assert "250.50" in driver.page_source
    finally:
        driver.quit()
