import requests
from bs4 import BeautifulSoup

cityList=[]
tempList=[]

source= requests.get('https://www.timeanddate.com/weather/india')
source.raise_for_status()
soup= BeautifulSoup(source.text, 'html.parser')
cities= soup.find_all('td')
temps = soup.find_all('td', class_='rbi')

for city in cities:

    if(city.a != None):
        name= city.a.text
        cityList.append(name)

for temp in temps:
    tempList.append(temp.text[0:2])
    
final= dict(zip(cityList,tempList))
s= sorted(final.items(),key = lambda x:x[1])

print('Coolest city: {} with {}\u00B0C\nHottest city: {} with {}\u00B0C'.format(s[0][0],s[0][1],s[len(s)-1][0],s[len(s)-1][1]))