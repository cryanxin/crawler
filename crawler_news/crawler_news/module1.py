# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
import pymysql
from Queue import Queue
from urlparse import urljoin
class crawler:
    def __init__(self):
        self.que=Queue()
        self.conn=pymysql.connect(host='localhost',user='root',passwd='19980415',db='news',charset='utf8')
        self.cur=self.conn.cursor()
    def createtable(self,dbname):
        self.cur.execute("CREATE TABLE urllist (urlid INT,url TEXT);")
        self.cur.execute("CREATE TABLE  url_ML(urlid INT,file LONGTEXT);")
        self.cur.execute("CREATE TABLE  url_Title(urlid INT,title LONGTEXT);")
    def crawler(self,pages,depth):
        for i in range(depth):
            newpage=[]
            for page in pages:
                try:
                    c=urllib2.urlopen(page)
                except:
                    print "Could not open %s"%page
                    continue
                self.cur.execute("INSERT INTO urlist ( url) VALUES( '%s' );"%page)
                soup=BeautifulSoup(c)
                links=soup("a")
                title=soup.find_all(div,class_="newstitle")
                self.cur.execute("INSERT INTO url_Title( title) VALUES( '%s' );"%title.text)
                context=soup.find_all(divmod,class_="newsContnet")
                self.cur.execute("INSERT INTO url_ML (file) VALUES( '%s' );"%context.text)
                for link in links:
                    url=urljoin(page,link["href"])
                    if url[0:24]=="http://news.hitwh.edu.cn":
                        self.que.put(url)
                        newpage.append(url)
        pages=newpages
        while not self.que.empty():


                   


        