#coding=utf8

import os
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("daobu.html",encoding='UTF-8'))

taglist = soup.find_all('td')#, attrs={'class': re.compile("(odd)|()")})
#print(taglist)
#print(soup.prettify())
gits=[]
names=[]
books={}

#flag = 0
for i in taglist:
    if i.text.startswith('KR'):
        gits.append(i.text)
    else:
        names.append(i.text)
    #books[str(i.text)]=books[str(i.text)]
    #print(i.text)
    #flag=flag+1

#print(gits)
#print(names)
for i in range(len(gits)):
    #print(gits[i])
    #print(type(names[i]))
    books[gits[i]] = names[i]

#print(books)

for i in books:
    print(i,books[i])
    os.system('mkdir test/'+books[i])
    os.system('git clone https://github.com/kanripo/'+i+'.git test/'+books[i])
   
