''''
script to convert json to csv 
'''

import json
import csv
import pandas as pd


#################################################
# converting meta json to csv
#################################################

with open('meta.json') as json_file:
    meta=json.load(json_file)
    
meta_data=meta['meta']

data_file=open('meta.csv','w')
csv_writer=csv.writer(data_file)

count=0
for meta in meta_data:
    if count==0:
        header=meta.keys()
        csv_writer.writerow(header)
        count+=1
    csv_writer.writerow(meta.values())
data_file.close()


#################################################
# converting events json to csv
#################################################

with open('events.json') as json_file:
    events=json.load(json_file)
    
events_data=events['events']

data_file_events=open('events.csv','w')
csv_writer_events=csv.writer(data_file_events)

count=0
for events in events_data:
    if count==0:
        header=events.keys()
        csv_writer_events.writerow(header)
        count+=1
    csv_writer_events.writerow(events.values())
data_file_events.close()