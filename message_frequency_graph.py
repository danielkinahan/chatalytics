#!/usr/bin/python3

import argparse
import sys
import glob
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import collections
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('directory') 
parser.add_argument('-m', action='store_false', help='Hide all messages')
parser.add_argument('-l', action='store_true', help='Display all photo and stickers links')
parser.add_argument('-t', action='store_true', help='Display all timestamps')
parser.add_argument('-n', action='store_true', help='Display all nicknames changes')
parser.add_argument('-T', action='store_true', help='Display all title changes')
parser.add_argument('-c', action='store_true', help='Display all changes to the group')
parser.add_argument('-r', action='store_true', help='Display all reactions')
args = parser.parse_args()

nickname = ('cleared the nickname for', 'cleared your nickname', 'set the nickname for', 'set your nickname', 'set his own nickname')
group = ('the group.', 'the group photo.', 'set the emoji to')
title = ('named the group', 'named the group')
skip = ('Click for video', 'points playing basketball.', 'Click for audio', 'Plan created:')

file_list = glob.glob('./' + args.directory + '/*.html')
file_list.sort()

total = []
names = {}
i=0

for filename in file_list:

	try:
		file = open(filename, "r")
	except e:
		perror(e)
		perror(args.filename + " could not be opened")
		exit(1)
	
	soup = BeautifulSoup(file, 'html.parser')
	messages = soup.find_all("div", class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")
	
	
	for message in messages[1:]:
		line = message.find_all("div")
	
		if any(ele in line[1].text for ele in nickname):
			if args.n:
				s+=line[0].text + ": " + line[1].text
		elif any(ele in line[1].text for ele in group):
			if args.c:
				s+=line[0].text + ": " + line[1].text
		elif "named the group" in line[1].text:
			if args.T:
				s+=line[1].text.split("named the group ", 1)[1][:-1]
		elif any(ele in line[1].text for ele in skip):
			continue

			#line[0].text is sender
			#line[1].text is message
			#line[-1].text is timestamp
		datetime_object = datetime.strptime(line[-1].text, "%d %b %Y, %H:%M")
		if line[0].text not in names:
			names[line[0].text]=i
			total.append(i)
			total[i] = []
			i+=1
		#total[names[line[0].text]].append(datetime_object.date())
		#total[names[line[0].text]].append(datetime_object.strftime("%H"))
for a in names.keys():
	counter = collections.Counter(total[names[a]])
	plt.plot_date(sorted(counter.keys()), counter.values(), label = str(a), linestyle = '-')
plt.title(sys.argv[1][6:])
plt.xlabel('Time')
plt.ylabel('Messages sent')
plt.legend()
plt.show()