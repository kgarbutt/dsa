# open txt file & add individual words to a python list

count = []
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#with open('alice.txt', 'r') as lines:
with open('Pride_and_Prejudice.txt', 'r') as lines:
	#print(words.readline())
	for line in lines:
		words = line.split()
		for word in words:
			if word not in punctuations:
				if word.isalpha():
					if word not in count:
						count.append(word)
	
	print(count)
