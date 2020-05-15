# wikipedia page scraper and table extractor
# by David Unland
# March 2020

import requests
import pandas as pd
import lxml.html as lh

# %%
# -------------------------scraping wikipedia article --------------------------
source = requests.get('https://de.wikipedia.org/wiki/Liste_fossil-thermischer_Kraftwerke_in_Deutschland')

doc = lh.fromstring(source.content)  # load from url
tr_elements = doc.xpath('//tr')  # get table elements

# for x in range(1,len(tr_elements)):
#     print(tr_elements[x].text)

i = 0
col = []

for t in (tr_elements[0]):
    name=t.text_content()
    print('%d: %s'%(i, name))
    col.append((name,[]))
    i += 1

# ----------------------- table elements to dictionary -------------------------
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
# dict.keys()
#
# for key, value in dict.items():
#     print(key, value)

df=pd.DataFrame.from_dict(dict)
df


# %%
# ------------------------------ beautify the table ----------------------------
# remove line breaks from table headers
for oldName in (df.columns):
    if str(oldName)[-1:] == '\n':
        newName = (str(oldName)[:-1])
        print(newName)
        df = df.rename(columns={oldName:newName})

# remove line breaks from rows
# df = df.replace('\n', '', regex=True)

# %%
# -------------------------- table manipulations -------------------------------
#  trying to access single rows...
df.iloc[2]['KW-Name']
df.keys()
df_braunkohle_steinkohle = pd.DataFrame()
kw_names = []
for row in range(0, 293):
    print(df.iloc[row]['KW-Name'])
    kw_names.append(df.iloc[row]['KW-Name'])

df_sorted = pd.DataFrame(columns=df.keys())
df_sorted['KW-Name'] = kw_names
df_sorted['KW-Name'].iloc[0]

df_braunkohle_steinkohle = df['KW-Name'].iloc[0] # works
df_braunkohle_steinkohle = df['Brutto­leistungin MWel'].iloc[0] # works
df_braunkohle_steinkohle = df['Wärmeaus­kopplungin MWth'].iloc[1] # works
df_braunkohle_steinkohle = df['Energie­träger'].iloc[1] # funktioniert nach copy&paste aus df.keys() !
df_braunkohle_steinkohle = df['Standort'].iloc[:] # works
df_braunkohle_steinkohle = df['Bun­des­land'].iloc[:] # funktioniert nach copy&paste aus df.keys() !
df_braunkohle_steinkohle = df['Inbetrieb­nahme/Ertüchtigung'].iloc[0] # works
df_braunkohle_steinkohle = df['(geplante)Still­legung'].iloc[0] # works
df_braunkohle_steinkohle = df['Bemerkungen'].iloc[0] # works
df_braunkohle_steinkohle = df['Betreiber'].iloc[0] # works
df_braunkohle_steinkohle = df['Koordinaten'].iloc[0] # works

index = 0
for key in df.keys():
    print(index, key, df[key].iloc[0])
    index += 1

for key in df.keys():
    if (df_braunkohle_steinkohle[[3]] != 'Erdgas'):
        print(found)

df_braunkohle_steinkohle
df

# number of keys
count = 0
for item in df.items():
    count+=1

print(count)

# %%
# ---------------------------------- export as csv -----------------------------
df.to_csv('liste-thermisch-fossiler-kraftwerke.csv')
