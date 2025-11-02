from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os, time

load_dotenv()
USER = os.getenv("INTRA_USER")
PASS = os.getenv("INTRA_PASS")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=Options()
)

driver.get("https://www.intranetmall.com/boulevardshoppingvilavelha4/")

wait = WebDriverWait(driver, 10)
print("Página:", driver.title)

try:
    user_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Usuário') or contains(@id,'user')]")))
    pass_field = driver.find_element(By.XPATH, "//input[@type='password']")
    login_btn  = driver.find_element(By.XPATH, "//button[contains(.,'Entrar') or contains(.,'Login')]")

    user_field.send_keys(USER)
    pass_field.send_keys(PASS)
    login_btn.click()

    print("Login enviado.")
    time.sleep(3)
    driver.save_screenshot("pos_login.png")

except Exception as e:
    print("Erro:", e)

driver.quit()
