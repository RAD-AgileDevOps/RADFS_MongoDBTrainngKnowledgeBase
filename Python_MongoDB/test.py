import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # for localhost instance

'''

If using Atlas cluster, please use th following connection string
  client = pymongo.MongoClient(<Atlas connection string>)

'''


# Getting a Database

db = client.CORD19     # here I am using the databses I created for analyssi of COVID19 datasets from the ECDC https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
db.list_collection_names()

'''

outputs (as per my system):
['col_ecdcCOVID19_20200622', 'col_ecdcCOVID19_20200611', 'ecdc_download_20200528_0748', 'col_ecdcCOVID19_20200529', 
'col_ecdcCOVID19_20200615', 'ecdc_download_20200529_0316am', 'radfs_poc20200623', 'col_ecdcCOVID19_20200609', '20200418', 
'col_ecdcCOVID19_20200626', 'covid_live_dataset', 'col_ecdcCOVID19_20200608', 'ecdc_download_20200527_2115', 'ecdc_download_202000603',
'col_ecdcCOVID19_20200612.json', 'col_ecdcCOVID19_20200629.', 'ecdc_download_20200419', 'col_ecdcCOVID19_20200630', 'ecdcCOVID19_20200617.json', 
'ecdc_download_20200530', 'col_ecdcCOVID19_20200628', 'sales', 'col_ecdcCOVID19_20200705', 'ecdc_download_202000601', 'col_ecdcCOVID19_20200623', 
'ecdcCOVID19_20200606', 
'tbl_ecdcCOVID19_20200607', 'col_ecdcCOVID19_20200627', 'col_ecdcCOVID19_20200610', 'col_ecdcCo19(20200624']




''
C:\Users\radfi>mongo
MongoDB shell version v4.2.2
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("830cdbc3-37ea-44e7-92c7-967a694f457c") }
MongoDB server version: 4.2.2
Server has startup warnings:
2020-12-09T06:13:32.302-0400 I  CONTROL  [initandlisten]
2020-12-09T06:13:32.302-0400 I  CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2020-12-09T06:13:32.302-0400 I  CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2020-12-09T06:13:32.302-0400 I  CONTROL  [initandlisten]
MongoDB Enterprise > show databases
CORD19                         0.086GB
M220_Exam_Q_no5                0.000GB
NodeJs_training_material       0.000GB
admin                          0.000GB
aggregation_example            0.000GB
book_inventory                 0.000GB
bulk_example                   0.000GB
config                         0.000GB
db                             0.000GB
dynamic1group_db               0.000GB
examples                       0.000GB
inventory_data_entry_tracking  0.000GB
local                          0.000GB
mongo_Final_exam_M221          0.000GB
radfs101_import_tool           0.001GB
radfsProofOfConcept            0.000GB
radfs_hello_world              0.000GB
test                           0.006GB
test_database                  0.000GB
training_mongo                 0.000GB
'''

