from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import wget
import json
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
\033[31m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░████░░░░
░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░
░░░░░░░░░░░░░░░█████████░░░░█░░░
░░░░░░░░░░░░░░░██░░░░░░█░░░░█░░░
░░░░░░░░░░░░░░░██░░░░░░░████░░░░
░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░
░░░░░░░░░░░░░██████░░░░░░░░░░░░░
░░░█████░░███░░░░░░███░░█████░░░
░░█░░░████░░░░░░░░░░░░████░░░█░░
░█░░░█░░░░░░░░░░░░░░░░░░░░█░░░█░
░█░██░░░░░███░░░░░░███░░░░░██░█░
░░██░░░░░░███░░░░░░███░░░░░░██░░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░█░░░
░░░█░░░░░░░░░░░░░░░░░░░░░░░░█░░░
░░░░█░░░░░░█░░░░░░░░█░░░░░░█░░░░
░░░░░█░░░░░░████████░░░░░░█░░░░░
░░░░░░███░░░░░░░░░░░░░░███░░░░░░
░░░░░░░░░████░░░░░░████░░░░░░░░░
░░░░░░░░██░░░██████░░░██░░░░░░░░
░░░░░░░█░█░░░░░░░░░░░░█░█░░░░░░░
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░
░░░░░░█░░█░░░░░░░░░░░░█░░█░░░░░░
░░░░░░░█░█░░░░░░░░░░░░█░█░░░░░░░
░░░░░░░░██░░░░░░░░░░░░██░░░░░░░░
░░░░░░░░░█░░░░░░░░░░░░█░░░░░░░░░
░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░
░░░░░░░░████░░░░░░░░████░░░░░░░░
░░░░░░░█░░░░█░░░░░░█░░░░█░░░░░░░
░░░░░░█░░░░░░█░░░░█░░░░░░█░░░░░░
░░░░░░████████████████████░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\033[0m
'''

def ascii_art_maker(link,color):
	
	colors = '''
	
	please select a color from this list:
	
	- \033[31mred    \033[0m
	- \033[32mgreen  \033[0m
	- \033[33myellow \033[0m
	- \033[34mblue   \033[0m
	- \033[35mmagenta \033[0m
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

	HTML = requests.get(url)

	soup = BeautifulSoup (HTML. text, 'html.parser')

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


def show_something(data_link):
	
	response = urlopen(data_link)
  
	x = json.loads(response.read())
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][0]['data']['title'],'\n')
	print(x['data']['children'][0]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][0]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][1]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][1]['data']['title'],'\n')
	print(x['data']['children'][1]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][1]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][2]['data']['title'],'\n')
	print(x['data']['children'][2]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][2]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][3]['data']['title'],'\n')
	print(x['data']['children'][3]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][3]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][4]['data']['title'],'\n')
	print(x['data']['children'][4]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][4]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][5]['data']['title'],'\n')
	print(x['data']['children'][5]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][5]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][6]['data']['title'],'\n')
	print(x['data']['children'][6]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][6]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][7]['data']['title'],'\n')
	print(x['data']['children'][7]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][7]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][8]['data']['title'],'\n')
	print(x['data']['children'][8]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][8]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][9]['data']['title'],'\n')
	print(x['data']['children'][9]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][9]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][10]['data']['title'],'\n')
	print(x['data']['children'][10]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][10]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][11]['data']['title'],'\n')
	print(x['data']['children'][11]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][11]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][12]['data']['title'],'\n')
	print(x['data']['children'][12]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][12]['data']['thumbnail'],'magenta')
		
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][13]['data']['title'],'\n')
	print(x['data']['children'][13]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][13]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][14]['data']['title'],'\n')
	print(x['data']['children'][14]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][14]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][15]['data']['title'],'\n')
	print(x['data']['children'][15]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][15]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][16]['data']['title'],'\n')
	print(x['data']['children'][16]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][16]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][17]['data']['title'],'\n')
	print(x['data']['children'][17]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][17]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][18]['data']['title'],'\n')
	print(x['data']['children'][18]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][18]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][19]['data']['title'],'\n')
	print(x['data']['children'][19]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][19]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][20]['data']['title'],'\n')
	print(x['data']['children'][20]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][20]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][21]['data']['title'],'\n')
	print(x['data']['children'][21]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][21]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][22]['data']['title'],'\n')
	print(x['data']['children'][22]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][22]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][23]['data']['title'],'\n')
	print(x['data']['children'][23]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][23]['data']['thumbnail'],'magenta')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][24]['data']['title'],'\n')
	print(x['data']['children'][24]['data']['thumbnail'],'\n')
	ascii_art_maker(x['data']['children'][24]['data']['thumbnail'],'magenta')

def get_hsl_playlist_link():

	hls_source = x[0]['data']['children'][0]['data']['secure_media']['reddit_video']['hls_url']

	mp4_link = ('https://savemp4.red/?url='+ hls_source )
	
	#https://savemp4.red/?url=
	
	
	print(banner)
	print('\n'+'subreddit_name: r/'+ x[0]['data']['children'][0]['data']['subreddit'],'\n')
	print('\n'+'hls_source: '+ x[0]['data']['children'][0]['data']['secure_media']['reddit_video']['hls_url'],'\n')
	#['subreddit'])
	choice = input('do you want to save the video as mp4 (y/n)')
	print('\n')
	if choice == 'y':
		print('\033[41m\033[30m')
		filename = wget.download(mp4_link)
		print('\033[0m')
		print('\n\n'+ filename +' saved succesfully !'+'\n')
	elif choice == 'n':
		exit()
	
	else:
		exit()
	
def get_gifs_and_images():
	
	print(banner)
	print('\n'+'subreddit_name: r/'+ x[0]['data']['children'][0]['data']['subreddit'],'\n')
	print(x[0]['data']['children'][0]['data']['url_overridden_by_dest'],'\n')
	#['subreddit'])
	choice = input('do you want to save the file(y/n)')
	print('\n')
	if choice == 'y':
		print('\033[41m\033[30m')
		filename = wget.download(x[0]['data']['children'][0]['data']['url_overridden_by_dest'])
		print('\033[0m')
		print('\n\n'+ filename +' saved succesfully !'+'\n')
	elif choice == 'n':
		exit()
	
	else:
		exit()
		
def get_text():
	print(banner)
	print('\n'+'subreddit_name: r/'+ x[0]['data']['children'][0]['data']['subreddit'],'\n')
	print(x[0]['data']['children'][0]['data']['selftext'],'\n')
	
if len(sys.argv) <= 1:
	
	print(banner)
	show_something('https://www.reddit.com/search.json?q=cats')

else:

	link = sys.argv[1]

	data_link = link[:link.find('?utm')][:-1] + '.json'
	
	response = urlopen(data_link)
  
	x = json.loads(response.read())
	
	try:
		get_hsl_playlist_link()
	except TypeError:
		try:
			get_gifs_and_images()
		except KeyError:
			get_text()
