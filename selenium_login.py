#-*- coding:utf8 -*-
from selenium import webdriver
from getpass import getpass

#user = input('Enter your username or email : ')
#password = getpass('Enter your password : ')
def login(url):
	user = ''
	password = ''

	driver = webdriver.Chrome(executable_path=r"/home/edu/analise_timeline/twitterRequestBots/chromedriver")
	driver.get(url)#muda seu valor dependendo da máquina

	user_box = driver.find_element_by_name('session[username_or_email]')#muda seu valor dependendo da máquina.
	user_box.send_keys(user)

	password_box = driver.find_element_by_name('session[password]')
	password_box.send_keys(password)

	login_button = driver.find_element_by_class_name('submit EdgeButton EdgeButton--primary EdgeButtom--medium')
	login_button.submit()

if __name__ == "__main__":

	url ='https://twitter.com/login?lang=pt'
	login(url)

#def scraping():

