from urllib.request import urlopen
import os
import datetime
import webbrowser

path = os.getcwd()
url = "url.txt"
urllink = "urllink.txt"
urllog= os.path.join(path,url)
urllinklog = os.path.join(path,urllink)

f= open(urllog, 'w')
f.close()
f= open(urllinklog, 'w')
f.close()

url = "https://urlhaus.abuse.ch/downloads/csv/"
response = urlopen(url)
headers = response.info()
output = response.read()

with open(urllog,'wb') as writefile:
    writefile.write(output)

Today = datetime.datetime.now()
day = 1
j =0

while j < day :
    j = j + 1
    Yesterday = datetime.timedelta(days=j)
    SampleDate = Today - Yesterday
    SampleFileDate = SampleDate.strftime("%Y-%m-%d")

    with open(urllog,'r') as readfile:
        content =readfile.readlines()

    for i in content :
        if SampleFileDate in i and "online" in i:
            httplink = i.split('","')
            with open(urllinklog,'a') as writefile :
                writefile.write(httplink[2]+"\n")
                
with open(urllinklog,'r') as readfile:
    content = readfile.readlines()
for link in content :
    webbrowser.open(link)