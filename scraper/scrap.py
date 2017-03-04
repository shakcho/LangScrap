from bs4 import beautifulsoup
import codecs
import re
import sys
import urllib2
# Requierd  argument of html file name and corpus_type
file_name = sys.argv[1]
corpus_type = sys.argv[2]

'''
Comment out code is for directly using with a URL
For our purpose we needed html file 
Change the code accordingly to get data directly from a URL 
'''
# url = urllib2.Request(url_name)
# page = urllib2.urlopen(url)
# soup = BeautifulSoup(page.read())

soup = BeautifulSoup(open(file_name),"html.parser")
text = soup.get_text('', strip=True)
if corpus_type.upper() == 'BENGALI':
	bengali_pattern = re.compile(ur'[\u0980-\u09FF ]+',re.UNICODE)
	cleandata = re.findall(bengali_pattern,text)
if corpus_type.upper() == 'HINDI':
	hindi_pattern = re.compile(ur'[\u0900-\u097F ]+',re.UNICODE)
	cleandata = re.findall(hindi_pattern,text)

# Saving the data to NewTextFIle.txt
f = open('NewTextFile.txt' , 'w')
for i in range(len(cleandata)):
	f.write(cleandata[i].encode('UTF-8'))


