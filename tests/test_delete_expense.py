from selenium import webdriver
from selenium.webdriver.common.by import By

def test_delete_expense():
    driver = webdriver.Chrome()
    try:
        driver.get("file:///C:/Users/yory/Desktop/ALURA/inmersion-dev-aula2-proyecto-base/index.html")
        driver.find_element(By.ID, "nombreGasto").send_keys("Transporte")
        driver.find_element(By.ID, "valorGasto").send_keys("100.00")
        driver.find_element(By.ID, "botonFormulario").click()
        
        botones_eliminar = driver.find_elements(By.XPATH, "//button[contains(text(), 'Eliminar')]")
        if botones_eliminar:
            botones_eliminar[0].click()
            driver.save_screenshot("reports/screenshots/test_delete_expense.png")
            assert "Transporte" not in driver.page_source
        else:
            assert False, "No se encontró el botón para eliminar."
    finally:
        driver.quit()
