#!/usr/bin/python3

#inbox/GARGBOYZ_uNSTploxvw/message_.html - file path to GARGBOYZ

import os
import sys
import itertools
import glob
from collections import Counter
from bs4 import BeautifulSoup

if not sys.argv[1]:
	perror("Please provide a directory")
	exit(1)

dir = sys.argv[1]
file_list = glob.glob('./' + dir + '/*.html')
file_list.sort()
groupnames = []
nicknames = []
words = []
names = {}
n = 0;
skip = ('the group.', 'the group photo.', 'set the emoji to', 'Click for video:', 'cleared the nickname for', 'cleared your nickname', 'points playing basketball.', 'Click for audio')
prepositions = ('i', 'I', 'the', 'to', 'you', 'it', 'a', 'is', 'and', 'u', 'my', "I'm", 'for', 'that', 'not', 'are', 'we', 'me', 'just', 'so', 'No', 'no', 'of', "don't", 'in', 'im', 'on')
for filename in file_list:
	try:
		file = open(filename, "r")
	except e:
		perror(e)
		perror(filename + " could not be opened")
		exit(1)

	soup = BeautifulSoup(file, 'html.parser')

	senders = soup.findAll('div',{'class':'_3-96 _2pio _2lek _2lel'})
	messages = soup.findAll('div',{'class':'_3-96 _2let'})
	
	for s,m in itertools.izip_longest(senders,messages):
		#print(s.text + ":" + m.text)
		
		if any(a in m.text for a in skip):
			continue
		elif "named the group" in m.text:
			groupnames.append(m.text)
		elif ("set your nickname to" or "set his own nickname to" or "set the nickname for") in m.text:
			nicknames.append(m.text)
		else:
			if s.text not in names:
				names[s.text] = n
				names[n] = s.text.encode("utf-8")
				words.append(n)
				words[n] = []
				n+=1
				
			for word in m.text.split():
				if word not in prepositions:
					words[names[s.text]].append(word.encode("utf-8"))
		
	file.close()
for i in range(0, len(names)/2):
	c = Counter(words[i])
	print(names[i], c.most_common(10))
#print(groupnames)
#print(nicknames)
	