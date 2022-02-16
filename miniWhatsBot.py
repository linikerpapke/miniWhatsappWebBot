from selenium import webdriver
import time

class whatsBot:
    def __inir__(self):
        self.mensagem = "Essa é uma mensagem automática"
        self.user = ["digite aqui o usuário", "outros"] #escolha exatamente o nome dos usuários que receberão a mensagem
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe') #baixe o driver do chrome compatível com seu navegador https://chromedriver.chromium.org/downloads

    def EnviarMensagns(self):

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30) # 30 segundos para ler o QR Code
        for user in self.user:
            user = self.driver.find_element_by_xpath(f"//span[@title='{user}']") #nome do usuário para quem a mensagem deve ser enviada
            time.sleep(3)
            user.click()
            escreveMsg = self.driver.find_element_by_class_name('p3_M1') #confira se a classe é igual no seu wpp web
            escreveMsg.send_keys(self.mensagem)
            time.sleep(2)
            sendBtn = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            sendBtn.click()
            time.sleep(5)

bot = whatsBot()
bot.EnviarMensagns()