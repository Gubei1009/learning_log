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


#米贝分享www.mibei77.com
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
    print(rs.text)
    return HttpResponse(rs.text)
