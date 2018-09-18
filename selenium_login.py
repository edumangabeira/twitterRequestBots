#-*- coding:utf8 -*-
from selenium import webdriver
from getpass import getpass
'''
Essa abordagem também não está sendo validada, por enquanto abre apenas uma página em branco,
sem logar na minha conta do twitter.


E se tentarmos entrar no twitter de um usuário já logado? Poderíamos usar o script de abrir uma sandbox 
e fazer uma pasta pra cada usuário
'''

#user = input('Enter your username or email : ')
#password = getpass('Enter your password : ')
def login(url):
	user = ''
	password = ''

	driver = webdriver.Chrome(executable_path=r"/home/edu/Downloads/chromedriver")
	driver.get(url)#muda seu valor dependendo da máquina

	user_box = driver.find_element_by_class_name('js-username-field email-input js-initial-focus')#muda seu valor dependendo da máquina.
	user_box.send_keys(user)

	password_box = driver.find_element_by_class_name('js-password-field')
	password_box.send_keys(password)

	login_button = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
	login_button.submit()

if __name__ == "__main__":

	url ='https://twitter.com/login?lang=pt'
	login(url)


