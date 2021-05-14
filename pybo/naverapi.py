# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import json
import os
import sys
import urllib.request

def naverbook(bookname):

    client_id = "mnw1ujtXRx8iVjlpmunC"
    client_secret = "ihjwsp7kJL"

    encText = urllib.parse.quote(bookname)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/book.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsontemp = json.loads(response_body.decode('utf-8'))
        print(jsontemp)
    else:
        print("Error Code:" + rescode)

    return jsontemp

def navermovie(moviename):

    client_id = "mnw1ujtXRx8iVjlpmunC"
    client_secret = "ihjwsp7kJL"

    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsontemp = json.loads(response_body.decode('utf-8'))
        print(jsontemp)
    else:
        print("Error Code:" + rescode)

    return jsontemp