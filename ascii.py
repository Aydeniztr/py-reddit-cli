from bs4 import BeautifulSoup
from urllib.requests import urlopen
import sys

source = ''



def ascii_art_maker(link,color):
	
	colors = '''
	
	please select a color from this list:
	
	- \u001b[31mred    \u001b[0m
	- \u001b[32mgreen  \u001b[0m
	- \u001b[33myellow \u001b[0m
	- \u001b[34mblue   \u001b[0m
	- \u001b[35magenta \u001b[0m
	- \u001b[36mcyan   \u001b[0m
	- \u001b[0mreset   \u001b[0m
	
	'''
	
	
	black = '\u001b[30m'
	red = '\u001b[31m'
	green = '\u001b[32m'
	yellow = '\u001b[33m'
	blue = '\u001b[34m'
	magenta = '\u001b[35m'
	cyan = '\u001b[36m'
	white = '\u001b[37m'
	reset = '\u001b[0m'
	
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
