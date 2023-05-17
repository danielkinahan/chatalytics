#!/usr/bin/python3

import argparse
import sys
import glob
import matplotlib.pyplot as plt
import collections
from datetime import datetime

from bs4 import BeautifulSoup

if not sys.argv[1]:
	perror("Please provide a directory")
	exit(1)

nickname = ('cleared the nickname for', 'cleared your nickname', 'set the nickname for', 'set your nickname', 'set his own nickname')
group = ('the group.', 'the group photo.', 'set the emoji to', 'named the group')
skip = ('Click for video', 'points playing basketball.', 'Click for audio', 'Plan created:')

dir = sys.argv[1]
file_list = glob.glob('./' + dir + '/*.html')
file_list.sort()
total = []

for filename in file_list:
	try:
		file = open(filename, "r")
	except e:
		perror(e)
		perror(filename + " could not be opened")
		exit(1)

	soup = BeautifulSoup(file, 'html.parser')
	messages = soup.find_all("div", class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")

	for message in messages[1:]:
		line = message.find_all("div")
		datetime_object = datetime.strptime(line[-1].text, "%d %b %Y, %H:%M")
		#total.append(datetime_object.date())
		#total.append(datetime_object.strftime("%H:%M")) broekn :(
	file.close()

counter = collections.Counter(total)
#for d,f in zip(counter.keys(), counter.values()):
#	print(str(d) + ": " + str(f))
plt.plot_date(sorted(counter.keys()), counter.values(), linestyle = '-')
plt.title(sys.argv[1][6:])
plt.xlabel('Time')
plt.ylabel('Messages sent')
plt.show()