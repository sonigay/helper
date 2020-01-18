#https://stu.goe.go.kr/edusys.jsp?page=sts_m42320
import urllib
from urllib.request import Request
import bs4
from datetime import datetime # 날짜 구하는거


def lunchtext():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://www.gunpo-ebiz.hs.kr/lunch.list?mcode=161311&cate=161311'
    print(url)
    print(datetime.today().day)  # 오늘 Day 값 가져옴
    today = datetime.today().day # 오늘날짜 구함
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    lunch1 = bsObj.find('div', {'id': 'foodListArea'})
    lunch2 = lunch1.find('tbody')
    lunch3 = lunch2.find_all('td')
    lunch4 = lunch3[today]
    lunch5 = lunch4.text
    lunchlen = len(lunch5)# 텍스트의 문자길이 구함
    itLunchlen = int(lunchlen)# 텍스트 문자길이 int형으로 변환
    if itLunchlen<=2: # 만약 길이가 2보다 작거나 같다면
        lunch5 = "없음"
    else:
        lunch5_1 = lunch4.find('div', {'class': 'lunch'})
        lunch5 = lunch5_1.text.strip()
    return lunch5

def lunchtextD1():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://www.gunpo-ebiz.hs.kr/lunch.list?mcode=161311&cate=161311'
    print(url)
    print(datetime.today().day)  # 오늘 Day 값 가져옴
    today = datetime.today().day # 오늘날짜 구함
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    lunch1 = bsObj.find('div', {'id': 'foodListArea'})
    lunch2 = lunch1.find('tbody')
    lunch3 = lunch2.find_all('td')
    lunch4 = lunch3[today+1]
    lunch5 = lunch4.text
    lunchlen = len(lunch5) # 텍스트의 문자길이 구함
    itLunchlen = int(lunchlen) # 텍스트 문자길이 int형으로 변환
    if itLunchlen<=2: # 만약 길이가 2보다 작거나 같다면
        lunch5 = "없음"
    else:
        lunch5_1 = lunch4.find('div', {'class': 'lunch'})
        lunch5 = lunch5_1.text.strip()
    return lunch5

def lunchtextD2():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://www.gunpo-ebiz.hs.kr/lunch.list?mcode=161311&cate=161311'
    print(url)
    print(datetime.today().day)  # 오늘 Day 값 가져옴
    today = datetime.today().day #오늘 날짜 구함
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    lunch1 = bsObj.find('div', {'id': 'foodListArea'})
    lunch2 = lunch1.find('tbody')
    lunch3 = lunch2.find_all('td')
    lunch4 = lunch3[today+2]
    lunch5 = lunch4.text
    lunchlen = len(lunch5) # 텍스트의 문자길이 구함
    itLunchlen = int(lunchlen)# 텍스트 문자길이 int형으로 변환
    if itLunchlen<=2: # 만약 길이가 2보다 작거나 같다면
        lunch5 = "없음"
    else:
        lunch5_1 = lunch4.find('div', {'class': 'lunch'})
        lunch5 = lunch5_1.text.strip()
    return lunch5

print(lunchtext())
print(lunchtextD1())
print(lunchtextD2())
