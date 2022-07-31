from distutils.fancy_getopt import wrap_text
import textwrap
import requests_html
import csv
session = requests_html.HTMLSession()


# enter the number of searches you want to do
num = int(input("Enter the number of searches you want to do: "))
srchData = []
paaData = []
answData = []
for i in range(num):
    data = input("Enter the data for search %s: " %(i+1))
    srchData.append(data)
def saveData(data):
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def get_paa(x):
    for item in r.html.xpath("/html/body/div[7]/div[1]/div[10]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[%s]"%(x)):
        # print(item.text)
        print("\n")
        data = item.text
        bagi = data.split("\n\n\n")
        print(bagi[0])
        
        bagi2 = bagi[0].split("\n")
        dt = bagi2[0].split(",")
        # write to csv
        xt = bagi2[1:]
        xc = str(textwrap.fill(xt[0], width=100))
        with open('data2.csv', 'a+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(dt)
            writer.writerow(xc.split(","))
            writer.writerow("\n")
for x in range(len(srchData)):   
    r = session.get('https://www.google.com/search?q='+srchData[x])
    r.html.render(sleep=5, timeout=8)
    for x in range(1, 5):
        get_paa(x)
