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
	#ngram = ngrams(data.split(),gram_value)
	ngram = ngrams(word_tokenize(data),gram_value)
	if gram_value == 1:
		for grams in ngram:
			ngramlist.append(grams[0])
			#ngramlist = word_tokenize(data)
	elif gram_value == 2:
		for grams in ngram:
			temp = grams[0] + " " + grams[1]
			ngramlist.append(temp)
	elif gram_value == 3:
		for grams in ngram:
			temp = grams[0] + " " + grams[1] + " " + grams[2]
			ngramlist.append(temp)
	elif gram_value == 4:
		for grams in ngram:
			temp = grams[0] + " " + grams[1] + " " + grams[2] + " " + grams[3]
			ngramlist.append(temp)
	return ngramlist

f = open(file_name,'r',encoding = 'utf-8')
data = f.read()
data_ngram = gen_ngram(data,gram_value)
my_dict = {}
for dg in data_ngram:
	if dg in my_dict:
		my_dict[dg] += 1
	else:
		my_dict[dg] = 1

year = year_value
new_dict = {}
for key in my_dict.keys():
	new_dict[key] = (year,my_dict.get(key))

with open('data.csv','a',encoding='utf-8') as f:
	csv.writer(f).writerows((k,) + v for k, v in new_dict.items())
