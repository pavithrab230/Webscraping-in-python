import requests
import csv
from bs4 import BeautifulSoup as bs

url = requests.get("http://www.tamilvu.org/ta/library-l1400-html-index-l1400i01-148065")
soup = bs(url.content, 'html.parser')

filename = "output1.csv"
csv_writer = csv.writer(open(filename,'w'))

for row in soup.find_all("row"):
    data=[]
    for th in tr.find_all("th"):
        data.append(th.text)
    if data:
        print("Inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue
    for td in tr.find_all("td"):
        if td.a:
            data.append(td.a.text.strip())
        else:
            data.append(td.text.strip())
    if data:
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)
        


