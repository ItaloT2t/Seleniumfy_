from tkinter import messagebox
from tkinter import messagebox
import functions


try:        
    functions.Seleniumfy().criar_playlist()
except:
    messagebox.showwarning('Erro', 'Falha na execução do robô. Entrar em contato com o Suporte') 
# webdriver.quit()























'''
    from selenium import webdriver

    def funcao_login(usuario, login):
        pass

    def abrir_site(url):
        # Cria uma nova instância do Google Chrome
        driver = webdriver.Chrome()

    def clicar_elemento(driver, xpath):
        # Encontra o elemento pelo seu XPath e clica nele
        elemento = driver.find_element("xpath", xpath)
        elemento.click()

    def preencher_campo(driver, xpath, texto):
        # Encontra o elemento pelo seu XPath e preenche com o texto fornecido
        elemento = driver.find_element("xpath", xpath)
        elemento.send_keys(texto)

    # Cria uma nova instância do Google Chrome
    driver = webdriver.Chrome()

    # Vai para a URL do Spotify
    driver.get("https://open.spotify.com/intl-pt")

    clicar_elemento(driver, "/html/body/div[5]/div/div[2]/div[1]/nav/div[2]/div[1]/div[1]/header/div/span/button/span/svg/path")

    # Preenche o campo de entrada com o XPath fornecid
    preencher_campo(driver, '//*[@id="text-input-3df080ec486aebfc"]', 'Minha Playlist')


    preencher_campo(driver,'html/body/div[29]/div/div/div/div[2]/div[3]/textarea', 'Uma playlist da musica'

    '''