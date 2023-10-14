import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
dwarf_table = soup.find_all("table")

temp_list = []
table_rows = dwarf_table[3].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

dwarf_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    dwarf_names.append(temp_list[i][0])
    distance.append(temp_list[i][1])
    mass.append(temp_list[i][2])
    radius.append(temp_list[i][3])

df = pd.DataFrame(list(zip(dwarf_names, distance, mass, radius)), columns=['dwarf_name','Distance','Mass','Radius'])
df.to_csv("brown_dwarfs.csv", index=False)