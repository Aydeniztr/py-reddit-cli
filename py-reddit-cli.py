from urllib.request import urlopen
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

def show_something(data_link):
	
	response = urlopen(data_link)
  
	x = json.loads(response.read())
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	
	
	print(x['data']['children'][0]['data']['title'],'\n')
	print(x['data']['children'][0]['data']['thumbnail'],'\n')
	
	print('\n')
	
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][1]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][1]['data']['title'],'\n')
	print(x['data']['children'][1]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][2]['data']['title'],'\n')
	print(x['data']['children'][2]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][4]['data']['title'],'\n')
	print(x['data']['children'][4]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][5]['data']['title'],'\n')
	print(x['data']['children'][5]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][6]['data']['title'],'\n')
	print(x['data']['children'][6]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][7]['data']['title'],'\n')
	print(x['data']['children'][7]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][8]['data']['title'],'\n')
	print(x['data']['children'][8]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][9]['data']['title'],'\n')
	print(x['data']['children'][9]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][10]['data']['title'],'\n')
	print(x['data']['children'][10]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][11]['data']['title'],'\n')
	print(x['data']['children'][11]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][12]['data']['title'],'\n')
	print(x['data']['children'][12]['data']['thumbnail'],'\n')
		
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][13]['data']['title'],'\n')
	print(x['data']['children'][13]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][14]['data']['title'],'\n')
	print(x['data']['children'][14]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][15]['data']['title'],'\n')
	print(x['data']['children'][15]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][16]['data']['title'],'\n')
	print(x['data']['children'][16]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][17]['data']['title'],'\n')
	print(x['data']['children'][17]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][18]['data']['title'],'\n')
	print(x['data']['children'][18]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][19]['data']['title'],'\n')
	print(x['data']['children'][19]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][20]['data']['title'],'\n')
	print(x['data']['children'][20]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][21]['data']['title'],'\n')
	print(x['data']['children'][21]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][22]['data']['title'],'\n')
	print(x['data']['children'][22]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][23]['data']['title'],'\n')
	print(x['data']['children'][23]['data']['thumbnail'],'\n')
	
	print('\n')
	
	print('\033[31m'+'\n'+'subreddit_name: '+ x['data']['children'][0]['data']['subreddit_name_prefixed'],'\n'+'\033[0m')
	print(x['data']['children'][24]['data']['title'],'\n')
	print(x['data']['children'][24]['data']['thumbnail'],'\n')

def get_hsl_playlist_link():

	print(banner)
	print('\n'+'subreddit_name: r/'+ x[0]['data']['children'][0]['data']['subreddit'],'\n')
	print(x[0]['data']['children'][0]['data']['secure_media']['reddit_video']['hls_url'],'\n')
	#['subreddit'])
	#choice = input('do you want to save the file(y/n)')
	#print('\n')
	#if choice == 'y':
		#print('\033[41m\033[30m')
		#filename = wget.download(x[0]['data']['children'][0]['data']['secure_media']['reddit_video']['hls_url'])
		#print('\033[0m')
		#print('\n\n'+ filename +' saved succesfully !'+'\n')
	#elif choice == 'n':
		#exit()
	
	#else:
		#exit()
	
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
