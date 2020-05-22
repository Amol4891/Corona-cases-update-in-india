# import all requird lib

import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Extract Data From the Website
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]

URL = 'https://www.mohfw.gov.in/'

# create column header
SHORT_HEADERS = ['SR.NO', 'STATE', 'INDIAN CONFIRMED',
                 'FOREIGN-CONFIRMED', 'CURED', 'DEATH']
response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))
states = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if stat:
        if len(stat) == 5:
            # Last Row
            stat = ['', *stat]
            states.append(stat)
        elif len(stat) == 6:
            states.append(stat)
states[-1][1] = "Total cases"
states.remove(states[-1])

# Table Formation
object = []
for row in states:
    object.append(row[1])
v_pos = np.arange(len(object))
performance = []
for row in states:
    performance.append(str(row[2]) + str(row[3]))
table = tabulate(states, headers=SHORT_HEADERS)
print(table)

# Plot the Graph
plt.barh(v_pos, performance, align='center', alpha=0.5,
         color=(234 / 256.0, 128 / 256.0, 252 / 256.0),
         edgecolor=(106 / 256.0, 27 / 256.0, 154 / 256.0))
plt.yticks(v_pos, object)
plt.xlim(1, 80)
plt.xlabel('Number of Cases ')
plt.title("Corona Virus Cases")
plt.show()
