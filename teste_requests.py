#-*- coding:utf8 -*-
import oauth2 as oauth
import requests
import time
import selenium
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import getpass

#Se conecta a uma sessão do twitter.
def login(payload, post_url_login, request_url):
	#click_payload = {'authenticity':'b0d7f51f3227a7d63f8701fdc98f19111212f421'}
	fake_browser = UserAgent()
	headers = {'User-Agent':str(fake_browser.chrome)}
	session = requests.Session()
	
	post_login = session.post(post_url_login, headers = headers, data = payload)
	get = session.get(request_url, headers = headers)
	arq2 = open("text.html","w")
	print (get.text)
	arq2.write(get.text)
	arq2.close()
	print ("FIM")

'''
Pega os 20 primeiros tweets a cada uma hora

#<div class='stream'> ==$0 

- É nesta div acima que está contida a timeline do twitter.

- Outra utilidade é a div abaixo que contém o json que precisamos para achar informações importantes
como o tweet_id, seu permalink, screen_name, data_you_follow, 

<div class = "tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards dismissible-content has-content">

<div class = "tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content
       original-tweet js-original-tweet
      
      
       has-cards dismissible-content has-content">

 - Os tweets promovidos possuem a tag abaixo para a mesma situação:

 <div class = "tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet promoted-tweet has-cards has-content presented scribed>


 - entra em div-class-stream

'''
'''
def retrieveTweets(request_url):

	while(True):

		soup = BeautifulSoup(request_url,"html.parser")
		div_tags = soup.find_all("div")
		
		for div in div_tags:
			if(div['class'] == "stream"):
				ol_tags = soup.find_all("ol")
				
				for ol in ol_tags:
				#if(div.['class'] != 'dismiss-module'):

		time.sleep(3600)
'''
'''
[GRUPO 1] curte/retweeta algumas das publicações das páginas que o usuário do GRUPO 1 segue

'''
#def generateBiasRight():

'''
[GRUPO 2]curte/retweeta algumas das publicações das páginas que o usuário do GRUPO 2 segue
'''

#def generateBiasLeft():

if __name__ == "__main__":

	bias_set = {
	'Bot1':1, 'Bot2':2,'Bot3':2,'Bot4':1,'Bot5':1,'Bot6':2,'Bot7':1, 'Bot8':2,'Bot9':2
	}

	post_url_login = "https://twitter.com/login"
	request_url = 'https://twitter.com'
	#user = input("entre com seu usuario do twitter:\n")
	#password = getpass("digite sua senha:\n")
	user = ""
	password = ""

	payload ={
		'session[username_or_email]':user,
		'session[password]':password
	}
	
	#A partir deste passo o usuário já deve estar logado
	login(payload,post_url_login, request_url)

	#coletando a página
	#retrieveTweets()

	'''
	Para cada tweet eu quero que seja extraído o texto, hora de coleta, hora da publicação, quantidade de curtidas e retweets.

	Ainda estou pensando na melhor forma de registrar isso, acredito que seja num csv com esses campos.
	'''
	'''for tweet in tweets:

		text = 
		favorite_count = 
		retweets =
		impression_order =
		published_time =
	'''
	#agora iremos gerar o viés de cada um
	'''if( bias_set['bot1'] == 1):
		generateBiasRight()

	else:
		generateBiasLeft()'''



