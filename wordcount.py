# count words in poem
import re
from collections import Counter

def word_count(filename):
	word_dict = {}

	text = open(filename, "r")
	for line in text:
		line = line.rstrip()
		line = re.sub(r'[^\w\s]','',line)
		line = line.lower()
		line = line.split(" ")
		for word in line:
			word_dict[word] = word_dict.get(word, 0) + 1
	for key, value in word_dict.items():
		print (key, value)	
	return word_dict

word_count("test.txt")


# Further Study
def counter_count(filename):
	
	text = open(filename, "r")
	big_list = []
	for line in text:
		line = line.rstrip()
		line = re.sub(r'[^\w\s]','',line)
		line = line.lower()
		line = line.split(" ")
		for word in line:
			big_list.append(word)
	word_dict = Counter(big_list)
	print (word_dict)

counter_count("test.txt")

	

