from bs4 import BeautifulSoup
from urllib.requests import urlopen
import sys

source = 'https://i.redd.it/eux9fe9pla981.jpg'



def ascii_art_maker(link,color):
	
	colors = '''
	
	please select a color from this list:
	
	- \033[31mred    \033[0m
	- \033[32mgreen  \033[0m
	- \033[33myellow \033[0m
	- \033[34mblue   \033[0m
	- \033[35magenta \033[0m
	- \033[36mcyan   \033[0m
	- \033[0mreset   \033[0m
	
	'''
	
	
	red     =  '\033[31m'
	green   =  '\033[32m'
	yellow  =  '\033[33m'
	blue    =  '\033[34m'
	magenta =  '\033[35m'
	cyan    =  '\033[36m'
	reset   =  '\033[0m'
	
	stock_char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	char_set_1 = 'BS#&@$%*!:.'
	
	url = 'https://www.degraeve.com/img2txt-yay.php?url='+link+'&mode=A&size='+'100'+'&charstr='+stock_char_set+'&order=O&invert=Y'

	HTML = urlopen(url)

	soup = BeautifulSoup (HTML.read(), 'html.parser')

	art = soup.find('pre').text
	
	if color == 'red':
		print (red)
		print(art)
		print(reset)
	
	elif color == 'green':
		print(green)
		print(art)
		print(reset)
		
	elif color == 'yellow':
		print(yellow)
		print(art)
		print(reset)
		
	elif color == 'blue':
		print(blue)
		print(art)
		print(reset)
	
	elif color == 'magenta':
		print(magenta)
		print(art)
		print(reset)
	
	elif color == 'cyan':
		print(cyan)
		print(art)
		print(reset)
		
	elif color == 'reset':
		print(reset)
		print(art)
		print(reset)
		
	else: 
		print(colors)
	
ascii_art_maker(source,'reset')
