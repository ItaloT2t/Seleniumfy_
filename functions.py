from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


@staticmethod
def pesquisar_musica(driver, spotify, artista_nome, musica_nome):
    time.sleep(1.5)
    try:
        campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/section/div/div/input')
        campo_pesquisa.clear()
        time.sleep(0.5)
        campo_pesquisa.send_keys(f"{artista_nome} {musica_nome}")
        print(f"Pesquisando {artista_nome} + {musica_nome}")
        time.sleep(2.5)
        print(f"Tentando clicar no elemento...")
        spotify.clicar_elemento(driver, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
        # print(f"Tentativa 2.")
        # Seleniumfy.clicar_elemento(driver, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
        # print(f"Clicado.")
    except:
        print(f"Entrando no except")
        body = driver.find_element(By.CSS_SELECTOR, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        print(f"rolei pra baixo")
        try:
            # body.send_keys(Keys.PAGE_DOWN)
            # print(f"rolei de novo")
            time.sleep(1.5)
            print(f"Tentando clicar")
            spotify.clicar_elemento(driver, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/div/div[4]/button')
        except:
            try:
                time.sleep(0.5)
                spotify.clicar_elemento(driver, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
            except:
                print(f"Não conseguiu clicar. Rolando pra cima...")
                body.send_keys(Keys.PAGE_UP )
                #isso volta print(f"rolei pra CIMA")
                time.sleep(1.5)
                #isso volta body.send_keys(Keys.PAGE_UP)
                print(f"rolei de novo")
                time.sleep(1.0)
                #time.sleep(1.5)
                #Seleniumfy.clicar_elemento(driver, '/html/body/div[5]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[3]/button')
    
        # campo_pesquisa.clear()
        # time.sleep(0.5)
        # campo_pesquisa.send_keys(f"{artista_nome} {musica_nome}")
        # time.sleep(1.5)
        # Seleniumfy.clique_elemento(driver, '/html/body/div[5]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[3]/button')
        '''try: 
            time.sleep(2)
            driver.execute_script("arguments[0].click();", elemento)
            print(f"Incluindo {artista_nome} + {musica_nome}")
        except:
            time.sleep(2)
            Seleniumfy.clicar_elemento_tentativas(driver, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')         '''
    
        #campo_pesquisa.send_keys(Keys.RETURN)
        # O TRY E EXCEPT DE BAIXO É O ULTIMO.
    '''
    try:
        elemento = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
        driver.execute_script("arguments[0].click();", elemento)
    except:
        elemento = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
        driver.execute_script("arguments[0].scrollIntoView();", elemento)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", elemento)
    print(f"Incluindo {artista_nome} + {musica_nome}")''' # ACABA AQUI

    
    ''' TRY DE  pesquisar_musica()

    try:
        spotify.clicar_elemento(driver, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
    except:
        elemento = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
        driver.execute_script("arguments[0].scrollIntoView();", elemento)
        time.sleep(2)
        spotify.clicar_elemento(driver, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button')
    print(f"Incluindo {artista_nome} + {musica_nome}")'''

class Seleniumfy:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.musicas = [
        {
            "artista": "Bon Jovi",
            "musica": "Livin on a prayer"
        },
        {
            "artista": "Bon Jovi",
            "musica": "You give love a bad name"
        },
        {
            "artista": "Bon Jovi",
            "musica": "Always"
        },
        {
            "artista": "Bon Jovi",
            "musica": "Misunderstood"
        },
        {
            "artista": "Bon Jovi",
            "musica": "It’s my life"
        },
        {
            "artista": "Bon Jovi",
            "musica": "Never say good bye"
        },
        {
            "artista": "Bon Jovi",
            "musica": "These days"
        },
        {
            "artista": "Bon Jovi",
            "musica": "Thank you for loving me"
        },
        {
            "artista": "Bon Jovi",
            "musica": "Everyday"
        },
        {
            "artista": "Bon Jovi",
            "musica": "Runnaway"
        },
        {
            "artista": "Bon Jovi",
            "musica": "One wild night"
        },
        {
            "artista": "Bon Jovi",
            "musica": "I’ll be There for you"
        },
        {
            "artista": "Aerosmith",
            "musica": "Crazy"
        },
        {
            "artista": "Aerosmith",
            "musica": "I don’t wanna miss a thing"
        },
        {
            "artista": "Aerosmith",
            "musica": "Cryin"
        },
        {
            "artista": "Aerosmith",
            "musica": "Dream on"
        },
        {
            "artista": "Aerosmith",
            "musica": "Fly away from here"
        },
        {
            "artista": "Elton John",
            "musica": "Nikita"
        },
        {
            "artista": "Elton John",
            "musica": "Sacrifice"
        },
        {
            "artista": "Elton John",
            "musica": "Skyline pigeon"
        },
        {
            "artista": "Elton John",
            "musica": "Rocket man"
        },
        {
            "artista": "Elton John",
            "musica": "Your song"
        },
        {
            "artista": "Bryan Adams",
            "musica": "Heaven"
        },
        {
            "artista": "The calling",
            "musica": "Wherever you will go"
        },
        {
            "artista": "firewing",
            "musica": "Maniac"
        },
        {
            "artista": "roses",
            "musica": "Sweet child o’mine"
        },
        {
            "artista": "Beatles",
            "musica": "Come togheter"
        },
        {
            "artista": "Beatles",
            "musica": "Twist and shout"
        },
        {
            "artista": "Queen",
            "musica": "I Want to Break Free"
        },
        {
            "artista": "Nirvana",
            "musica": "Smells like teens spirit"
        }
        ]   
       

    '''
        showwarning()
        showerror()
        askquestion()
        askokcancel()
        askyesno ()
        askretrycancel ()
    '''

    # def funcao_login(usuario, login):

    # Cria uma nova instância do Google Chrome
    def abrir_site(url):
        driver = webdriver.Chrome()

    # Encontra o elemento pelo seu XPath e clica nele
    def clicar_elemento(self,driver, xpath):
        elemento = driver.find_element("xpath", xpath)
        elemento.click()
    
    def clicar_elemento_tentativas(self, driver, xpath):
        for _ in range(2):  # Tenta clicar duas vezes
            try:
                elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                elemento.click()
                break
            except NoSuchElementException:
                # Rola a barra de rolagem para baixo se não encontrar o elemento
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
        else:
            # Se ainda não encontrou o elemento, rola a barra de rolagem para cima até o topo
            driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
            try:
                elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                elemento.click()
            except NoSuchElementException:
                print(f"Elemento com o xpath {xpath} não encontrado.")



    def Esperar_clicar_elemento(self,driver, by, xpath):
        elemento = WebDriverWait(driver, 820).until(EC.visibility_of_element_located((by, xpath)))
        elemento.click()

    def preencher_campo(self,driver, xpath, texto):
        # Encontra o elemento pelo seu XPath e preenche com o texto fornecido
        elemento = driver.find_element("xpath", xpath)
        elemento.send_keys(texto)

    #driver = webdriver.Chrome()

    def criar_playlist(self):
        # Vai para a URL do Spotify
        self.driver.get("https://open.spotify.com/intl-pt")
        # Altera o nível de zoom para 30%
        self.driver.execute_script("document.body.style.zoom='100%'")
        self.driver.set_window_size(1920, 8000)
        time.sleep(3)
        self.clicar_elemento(self.driver, '/html/body/div[3]/div/div[2]/div[3]/header/div[5]/button[2]/span')
        time.sleep(5)
        self.clicar_elemento(self.driver, '/html/body/div[1]/div/div[2]/div/div/ul/li[2]/button/span[2]')
        time.sleep(6)
        self.preencher_campo(self.driver, '//*[@id="email"]', 'login')
        #//*[@id="email"]
        #/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input

        self.preencher_campo(self.driver, '//*[@id="pass"]', 'senha')
        time.sleep(1)
        self.clicar_elemento(self.driver, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button')
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(15)
        self.clicar_elemento(self.driver, '//*[@id="main"]/div/div[2]/div[1]/nav/div[2]/div[1]/div[1]/header/div/span/button') # + PLAYLIST
        time.sleep(1)
        self.clicar_elemento(self.driver,'//*[@id="context-menu"]/ul/li[1]/button/span')

        time.sleep(5)
        self.clicar_elemento(self.driver,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[1]/div[5]/span[2]/button/span/h1')
        # Preenche o campo de entrada com o XPath fornecid
        time.sleep(2)
        self.preencher_campo(self.driver, '/html/body/div[24]/div/div/div/div[2]/div[2]/input', 'Playlist T2T')
        time.sleep(1)
        self.preencher_campo(self.driver,'/html/body/div[24]/div/div/div/div[2]/div[3]/textarea', 'musicas')
        time.sleep(1)
        self.clicar_elemento(self.driver,'/html/body/div[24]/div/div/div/div[2]/div[4]/button/span')
        
        time.sleep(3)
        for musica in self.musicas:
            pesquisar_musica(self.driver, self, musica['artista'], musica['musica'])
            time.sleep(2)
        messagebox.showinfo('SeleniumFy:', 
        'Playlist criada com Sucesso.')
        self.driver.quit
        
