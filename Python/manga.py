import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import shutil
import re

name = raw_input("Enter comic name")
chapter = raw_input("Enter chapter number")
chapter = int(chapter)
x = 1
z = 0
destinationDir = name+' '+str(chapter)

if not os.path.exists(destinationDir): 
				os.makedirs(destinationDir)
			
for y in range(0,50):
	url = "http://mangahit.com/"+name+"/"+str(chapter)+"/"+str(x)
	html = urllib2.urlopen(url)
	data=html.read()
	soup = BeautifulSoup(data)
	for link in soup.find_all('img'):
		y=(link.get('src'))
		print y
		z=z+1
		if(z==1):
			break
	urllib.urlretrieve(y,'page'+str(x)+'.jpg')	
	print("Downloaded page"+str(x))	
	
	z=0
	shutil.move('page'+str(x)+'.jpg', destinationDir)
	x=x+1
print("Completed downloading! Have fun reading!");
