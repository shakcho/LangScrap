import sys
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import csv
'''
Requierd argument 
1. 	Text file consists of linugstic data 
	Filename should be in the form of year.txt where year can be any 4 digit integr
2. 	N value of N-gram 
	N can be 1 to 4 .
'''

file_name = sys.argv[1]
gram_value = int(sys.argv[2])
year_value = file_name[:4]

def gen_ngram(data,gram_value):
	ngramlist = []
	ngram = ngrams(data.split(),gram_value)
	if gram_value == 1:
		for grams in ngram:
			ngramlist.append(grams[0])
			#ngramlist = word_tokenize(data)
	return len(ngramlist)

f = open(file_name,'r',encoding = 'utf-8')
data = f.read()
total_count = gen_ngram(data,gram_value)

year = year_value
new_dict = {year:total_count}

with open('total_count.csv','a',encoding='utf-8') as f:
	csv.writer(f).writerows((k,v) for k,v in new_dict.items())
