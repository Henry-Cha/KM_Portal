import requests
from bs4 import BeautifulSoup


def check_standard():
    data = []
    url = "https://www.kmu.ac.kr/uni/main/page.jsp?mnu_uid=143&"
    res = requests.get(url)
    xml = res.text

    soup = BeautifulSoup(xml, 'html.parser')
    datalist = soup.find('tbody').findAll('tr')
    for i in datalist:
        data.append(i.find('td', class_='subject').text)
        data.append(i.find('td', class_='subject').find('a')["href"])
        data.append(i.find('td', class_='writer').text)
        data.append(i.find('td', class_='date').text)
    return data