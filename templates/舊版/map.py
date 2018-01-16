from io import StringIO
import pandas as pd
import os
sys.path.append('C:\ProgramData\Anaconda3\Lib\site-packages')
import geocoder
import sys

df=pd.read_csv('10501.csv')

a=df.keys()
rownum=len(df)
print(rownum)
temp=[]
for s in range(1,rownum):
	
	
		
	temp.append((df['site_id'][s])+(df['village'][s]))

for add in temp:

    g = geocoder.arcgis(add)
    print(g.latlng)

		





