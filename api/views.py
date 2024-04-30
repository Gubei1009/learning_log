import base64
import re
import urllib.parse

import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse, HttpResponse


# Create your views here.


def parse(request):
    url = request.GET.get("url")
    rs = requests.get(url)
    beautiful_soup = BeautifulSoup(rs.text, "html.parser")
    dds = beautiful_soup.find_all("dd")
    content = []
    for dd in dds:
        charpter = {'name': dd.text, 'url': dd.find('a').get('href')}
        content.append(charpter)
    res = {"data": content}
    return JsonResponse(res)


# 米贝分享www.mibei77.com
def getFreeSS(request):
    url = request.GET.get("url")
    rs = requests.get(url)
    beautiful_soup = BeautifulSoup(rs.text, "html.parser")
    dd = beautiful_soup.find("h2", class_="entry-title").find("a").get("href")
    print(dd)
    rs = requests.get(dd)
    beautiful_soup = BeautifulSoup(rs.text, "html.parser")
    for e in beautiful_soup.find_all("p"):
        if e.text.startswith("http://mm.mibei77.com/"):
            print("文件路径：" + e.text)
            rs = requests.get(e.text)
            break

    base64_str = str(base64.b64decode(rs.text), "utf-8").replace("\r", "")
    # print(base64_str)

    res = ""
    oldStr = "(mibei77.com 米贝节点分享)"
    repStr = "(llh爬取)"
    for e in base64_str.split("\n"):
        # temp = ""
        temp = e.replace(urllib.parse.quote(oldStr), repStr)
        # print(temp==e)
        if (e == temp) & (e != ""):
            index = e.find("://")+len("://")
            start = e[:index]
            b64 =str(base64.b64decode(e[index:]),"utf-8")
            temp = b64.replace(oldStr, repStr)
            temp = str(base64.b64encode(temp.encode("utf-8")),"utf-8")
            # print("index "+index+"---e[index]==="+e[index]+"b64解码"+b64)
            temp = start + temp
            # print(temp)
        print(temp)
        res = res + temp+"\r"
    return HttpResponse(base64.b64encode(res.encode("utf-8")))
