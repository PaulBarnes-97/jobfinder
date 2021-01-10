import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.linkedin.com/jobs/search/?f_E=2&f_JT=F&f_LF=f_AL&f_TPR=r604800&geoId=103644278&keywords=software%20engineer&location=United%20States")
src = r.content
data = r.text
soup = BS(src, 'html.parser')
soupy = soup.prettify()

Job_Comp = []
#print(soup.prettify())
'''
links = soup.find('a')
for link in links:
    if "jobs" not in link.text and "Software" in link.text:
        Job_Comp.append(link.text)
        #print(link.text)
        #print(link.attrs['href'])
print(Job_Comp)
'''
sec_search = soup.find_all('div')
for result in sec_search:
    print(result.prettify())

