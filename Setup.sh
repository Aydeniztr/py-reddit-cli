printf '''
\033m[31mreddit-cli\033[0m

 beautifulsoup4
 requests

 required modules take (this much) space

 Note:if you have this module already you
 type `n` or press to ctrl+c 

want to install the required modules (y/n)

'''
read $choice


if [ $numb = "1" ]
then
pip install beautifulsoup4
pip install requests
else
