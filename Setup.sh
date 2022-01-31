echo '''
\033m[31mreddit-cli\033[0m

 beautifulsoup4
 requests

 required modules take (this much) space

 Note:if you have this module already you
 type `n` or press to ctrl+c 

want to install the required modules (y/n)

'''
read $choice
if $choice == 'y':
then echo '\033[35minstallation starded\033[0m'
then pip install beautifulsoup4
then pip install requests
then echo 'installation done \033[31m!!!\033[0m'
if $choice == 'n':
then echo 'exiting...'
