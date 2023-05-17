#!/usr/bin/python3

"""
Takes a fb messenger directory as cmd line input
Outputs a collage of images sorted by user who posted
"""

import sys
import os
import glob
import imageio

from bs4 import BeautifulSoup

if not sys.argv[1]:
	perror("Please provide a directory")
	exit(1)

dir = sys.argv[1]
file_list = glob.glob('./' + dir + '/*.html')
file_list.sort()

pic_list = [list() for f in range(10)]
users = []

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
		photos = line[1].find_all("img")
		if line[0].text in users:
			x=users.index(line[0].text)
		else:
			users.append(line[0].text)
			x=len(users)-1
		for i in photos:
			if i['src'][-3:]==("jpg" or "png"):
				pic_list[x].append(i['src'])
	file.close()
for user in users:
	images = []
	gif_file = "~/Desktop/ " + user[:5] + ".gif"
	for filename in pic_list[users.index(user)]:
		images.append(imageio.imread("../"+filename))
	imageio.mimsave(gif_file, images, duration=0.1)
