# put your code here.
"""
from sys import argv
print(argv)"""
def word_count(filename):
	text = open(filename)

	word_count_dict = {}
	for line in text:
		line = line.rstrip()
		line = line.split(" ")
		for word in line:
			#print(line)
			word_count_dict[word] = word_count_dict.get(word,0) + 1

	for key, value in word_count_dict.items():
		print("{} {}".format(key,value))

	text.close()

word_count("test.txt")