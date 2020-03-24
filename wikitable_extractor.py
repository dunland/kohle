import requests
# import bs4
import pandas as pd
import lxml.html as lh

source = requests.get('https://de.wikipedia.org/wiki/Liste_fossil-thermischer_Kraftwerke_in_Deutschland')

# content = bs4.BeautifulSoup(source.text, 'lxml')
doc = lh.fromstring(source.content)
tr_elements = doc.xpath('//tr')

i = 0
col = []

for t in tr_elements[0]:
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

dict={title:column for (title,column) in col}
df=pd.DataFrame(dict)
df
