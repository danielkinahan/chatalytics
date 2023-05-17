#!/usr/bin/python3

#inbox/GARGBOYZ_uNSTploxvw/ - file path to GARGBOYZ

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
words = {}
sentences = {}

skip = ('the group.', 'the group photo.', 'set the emoji to', 'Click for video:', 'cleared the nickname for', 'cleared your nickname', 'points playing basketball.', 'Click for audio')

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
		if any(a in m.text for a in skip):
			continue
		elif "named the group" in m.text:
			groupnames.append(m.text)
		elif ("set your nickname to" or "set his own nickname to" or "set the nickname for") in m.text:
			nicknames.append(m.text)
		elif s:
			if s.text in sentences:
				sentences[s.text] = 1 + sentences[s.text]
			else:
				sentences[s.text] = 1
			if not m:
				continue
			for word in m.text.split():
				if s.text in words:
					words[s.text] = 1 + words[s.text]
				else:
					words[s.text] = 1
	file.close()
total = sorted(sentences.items(), reverse=True, key=lambda x: x[1])
i=1
for item in total:
	print str(i) + ": " + item[0].encode("utf-8") + ": " + str(item[1]) + " messages, " + str(words[item[0]]) + " words"
	i+=1
#print(groupnames)
#print(nicknames)