from io import StringIO
import pandas as pd
import os
def get_lat():
	df=pd.read_csv('latlng.csv')
	citys=[]
	
	rownum=len(df)


	for s in range(1,rownum):
	
	
		citys.append(df['lat'][s])

	return citys
def get_lng():
	df=pd.read_csv('latlng.csv')
	citys=[]
	
	rownum=len(df)


	for s in range(1,rownum):
		
		
	
		

	
		citys.append(df['lng'][s])

	return citys

def get_town():
	df=pd.read_csv('10501.csv')
	citys=[]
	
	rownum=len(df)


	for s in range(1,rownum):
		temp={};
		
		temp['city']=str(df['site_id'][s])[:3]
		temp['area']=str(df['site_id'][s])[3:]
		temp['town']=str(df['village'][s])
		temp['value']=s
	
		citys.append(temp)

	return citys
def get_city():
	df=pd.read_csv('10501.csv')
	citys=[]
	
	rownum=len(df)


	for s in range(1,rownum):
		temp={};
		if str(df['site_id'][s])[:3]!=str(df['site_id'][s-1])[:3]:
			
			temp['city']=str(df['site_id'][s])[:3]

	
	
			citys.append(temp)
	
	return citys
def get_area():
	df=pd.read_csv('10501.csv')
	citys=[]
	
	rownum=len(df)


	for s in range(1,rownum):
		temp={};
		if str(df['site_id'][s])[3:]!=str(df['site_id'][s-1])[3:]:
			temp['city']=str(df['site_id'][s])[:3]
			temp['area']=str(df['site_id'][s])[3:]
			temp['value']=s
	
	
			citys.append(temp)
	
	return citys

		




