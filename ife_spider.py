#!usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

url = "http://ife.baidu.com/college/detail/id/5"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
result = soup.select('span[class="cal-list-info-detail"] > span' )
learninglist = []
learnedlist = []

for index in range(len(result)):
	if index % 3 == 1:
		learninglist.append(result[index].get_text())
	if index % 3 == 2:
		learnedlist.append(result[index].get_text())
	
for index in range(len(learnedlist)):
	print ('有%s人在学习该课程,有%s人已经完成该课程,完成率%.2f%%' % (learninglist[index], learnedlist[index], (int(learnedlist[index]) / int(learninglist[index])*100)))

