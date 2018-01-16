# coding: utf-8

import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
import csv
import os
import pymysql
import MySQLdb

engine = create_engine('mysql://root:12345678@localhost/testdb?charset=utf8')



for dirPath, dirNames, fileNames in os.walk('C:\\Users\\tcfst\\Desktop\\ss\\yearold\db\\yearold'):
     for f in fileNames:
        if f.find('.csv')!= -1:
            print (dirPath+'\\'+f)
            dfs=pd.read_csv(dirPath+'\\'+f,index_col=0)
            with engine.connect() as conn, conn.begin():
                dfs.iloc[1:].to_sql('yearold', conn, if_exists='append')