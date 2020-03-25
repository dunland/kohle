# wikipedia page scraper and table extractor
# by David Unland
# March 2020

import requests
import pandas as pd
import lxml.html as lh

source = requests.get('https://de.wikipedia.org/wiki/Liste_fossil-thermischer_Kraftwerke_in_Deutschland')

doc = lh.fromstring(source.content)
tr_elements = doc.xpath('//tr')

for x in range(1,len(tr_elements)):
    print(tr_elements[x].text)

i = 0
col = []

for t in (tr_elements[0]):
    i += 1
    name=t.text_content()
    print('%d: %s'%(i, name))
    col.append((name,[]))

#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    t_row=tr_elements[j]

    #i is the index of our column
    i=0

    #Iterate through each element of the row
    for t in t_row.iterchildren():
        data=t.text_content()
        print(data)

        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1

# col  # Tabelle
# col[0]  # Spalte
# col[0][0]  # Zeile
# col[0][0][0]  # Buchstabe
#
# col[:][0]  # Spalte 0 mit allen Zeilen
# col[0][0]  # KW-Name
# col[1][0]  # Bruttoleistung

dict={title:pd.Series(column) for (title,column) in col}
dict

df=pd.DataFrame.from_dict(dict)
df

# remove line breaks from table headers
for oldName in (df.columns):
    if str(oldName)[-1:] == '\n':
        newName = (str(oldName)[:-1])
        print(newName)
        df = df.rename(columns={oldName:newName})

# remove line breaks from rows
df = df.replace('\n', '', regex=True)
df = df.replace(r'\s', '', regex=True)  # removes all white spaces
df.to_csv('liste-thermisch-fossiler-kraftwerke.csv')
