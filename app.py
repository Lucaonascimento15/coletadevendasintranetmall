"""
acessar_intranet.py
Exemplo: abrir a página da intranet do Boulevard Shopping Vila Velha com Selenium.
Adaptar seletores de acordo com o HTML real (id, name, xpath, css etc).
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://www.intranetmall.com/boulevardshoppingvilavelha4/"

def criar_driver(headless: bool = False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")  # modo headless
        chrome_options.add_argument("--window-size=1920,1080")
    # opções úteis
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # inicializa driver (webdriver-manager baixa automaticamente o chromedriver compatível)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def exemplo_fluxo():
    driver = criar_driver(headless=False)  # troque para True se quiser sem abrir janela
    wait = WebDriverWait(driver, 15)  # tempo máximo de espera para elementos

    try:
        driver.get(URL)
        print("Página aberta:", driver.title)

        # --- Exemplo 1: clicar em um botão/link "ENTRAR" pelo texto do link ---
        try:
            # se o botão/link existir como um link com texto "ENTRAR"
            entrar = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "ENTRAR")))
            entrar.click()
            print("Cliquei em 'ENTRAR'.")
        except Exception as e:
            print("Botão/link 'ENTRAR' não foi encontrado pelo link text:", e)

        # --- Esperar e capturar o título / screenshot ---
        # aguardar que algum elemento do formulário apareça; adaptar o seletor conforme o site real
        time.sleep(1)  # pequena pausa para animações/JS
        driver.save_screenshot("intranet_home.png")
        print("Screenshot salva como intranet_home.png")

        # --- Exemplo 2: localizar campos de login e preencher (NÃO INSIRA CREDENCIAIS REAIS AQUI) ---
        # aqui damos exemplos de diferentes estratégias de localização. Use a que funcionar para o HTML real:
        campo_usuario = None
        campo_senha = None

        # Tentar localizar por id
        try:
            campo_usuario = driver.find_element(By.ID, "username")   # exemplo
            campo_senha  = driver.find_element(By.ID, "password")
            print("Campos encontrados por id.")
        except:
            pass

        # Tentar localizar por name (alternativa)
        if not campo_usuario:
            try:
                campo_usuario = driver.find_element(By.NAME, "username")
                campo_senha  = driver.find_element(By.NAME, "password")
                print("Campos encontrados por name.")
            except:
                pass

        # Tentar localizar por placeholder / xpath (mais robusto)
        if not campo_usuario:
            try:
                # localizar input que tenha placeholder contendo 'Usuário' ou 'Login' (exemplo)
                campo_usuario = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Usuário') or contains(@placeholder, 'Login') or contains(@id,'user')]")
                campo_senha  = driver.find_element(By.XPATH, "//input[@type='password']")
                print("Campos encontrados por xpath/placeholder.")
            except Exception as e:
                print("Não localizei automaticamente campos de login:", e)

        # Se achou os campos, preencher com placeholders
        if campo_usuario and campo_senha:
            campo_usuario.clear()
            campo_usuario.send_keys("lucas.nascimento")
            campo_senha.clear()
            campo_senha.send_keys("senhaqualquer")
            # exemplo de clique no botão de login (adaptar seletor)
            try:
                botao_login = driver.find_element(By.XPATH, "//button[contains(., 'Entrar') or contains(., 'Login')]")
                botao_login.click()
                print("Tentativa de login realizada (com credenciais de exemplo).")
            except Exception as e:
                print("Botão de login não encontrado automaticamente:", e)
        else:
            print("Campos de login não detectados automaticamente; inspecione o HTML e ajuste os seletores.")

        # --- Aguarda algum elemento que indique login bem-sucedido (exemplo) ---
        # Exemplo: aguardar por um elemento que só aparece após autenticação
        try:
            painel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".painel-usuario, #dashboard, .welcome")) )
            print("Elemento pós-login encontrado; presumivelmente logado.")
        except:
            print("Não identifiquei elemento pós-login; pode estar em tela de erro ou precisará de outro seletor.")

        # salvar outra screenshot depois
        time.sleep(1)
        driver.save_screenshot("intranet_pos_login.png")
        print("Screenshot pós-login salva como intranet_pos_login.png")

    finally:
        # manter aberto um pouco para você ver o navegador (remova em scripts headless)
        time.sleep(2)
        driver.quit()
        print("Driver encerrado.")

if __name__ == "__main__":
    exemplo_fluxo()
