# count words in poem
import re
from collections import Counter, OrderedDict


# def word_count(filename):
# 	word_dict = {}

# 	text = open(filename, "r")
# 	for line in text:
# 		line = line.rstrip()
# 		line = re.sub(r'[^\w\s]','',line)
# 		line = line.lower()
# 		line = line.split(" ")
# 		for word in line:
# 			word_dict[word] = word_dict.get(word, 0) + 1
# 	for key, value in word_dict.items():
# 		print (key, value)	
# 	return word_dict

# word_count("test.txt")


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
	return word_dict

def sorted_dict(word_dict):
	sorted_dict = OrderedDict(sorted(word_dict.items()))
	print(sorted_dict)	
	# sorted_dict = sorted(word_dict.keys())
	# for item in sorted_dict:
	# 	print (item, word_dict[item])

word_dict = counter_count("test.txt")
sorted_dict(word_dict)





	

