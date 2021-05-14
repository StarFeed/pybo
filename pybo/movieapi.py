import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import numpy as np
import pandas as pd

def Mrank():
    page = requests.get('https://movie.naver.com/movie/running/current.nhn')
    html = page.text
    soup = bs(html, 'lxml')
    result = soup.find_all('dl','lst_dsc')
    moviedata=[]
    cnt=0
    for temp in result:
        mdata = {}
        cnt+=1
        mdata['num'] = cnt
        #제목
        tdata = temp.find('dt', 'tit')
        tdata = tdata.find('a').text
        mdata['title'] = tdata
        #평점
        star = temp.find('div', 'star_t1')
        star = star.find('span','num').text
        mdata['star'] = star
        #장르
        genre = temp.find('dl', 'info_txt1')
        genre = genre.find('span','link_txt').text.replace('\n','').replace('\r','').replace('\t','')
        mdata['genre'] = genre
        moviedata.append(mdata)

    imgresult = soup.find_all('div', 'thumb')
    imgurl = []
    for temp in imgresult:
        url = temp.find('img')
        imgurl.append(url['src'])

    i=0
    for temp in moviedata:
        temp['img'] = imgurl[i]
        i+=1

    return moviedata