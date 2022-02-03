from requests_html import HTMLSession
import datetime
session = HTMLSession()
headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}
status_url= f'https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020191111&_cid=P11-KQ6CCK-39257-2'
html = session.get(status_url)
html = html.html
html = session.get(status_url)
print(html)
html = html.html
print("this is reaspnse html")
print(html)

thisval = html.find('div.ps-biblio-data',first= True)
print(thisval.text)
print(thisval)
publication= thisval[0].find('#detailMainForm:MyTabViewId:j_idt1683:j_idt1688').text
print(publication)
