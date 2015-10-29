import csv
import pandas as pd

# Extract different event_types into their own CSVs

events_train = pd.read_csv('../events_train.csv')

def getRelatedDataFrame(type):
	return events_train[events_train['event_type'] == type]

def saveCSV(df, name):
	df.to_csv('../e_' + name + '.csv')

events_accidentsIncidents = getRelatedDataFrame('accidentsAndIncidents')
events_roadwork = getRelatedDataFrame('roadwork')
events_precipitation = getRelatedDataFrame('precipitation')
events_deviceStatus = getRelatedDataFrame('deviceStatus')
events_obstruction = getRelatedDataFrame('obstruction')
events_trafficConditions = getRelatedDataFrame('trafficConditions')

saveCSV(events_accidentsIncidents, 'accidentsAndIncidents')
saveCSV(events_roadwork, 'roadwork')
saveCSV(events_precipitation, 'precipitation')
saveCSV(events_deviceStatus, 'deviceStatus')
saveCSV(events_obstruction, 'obstruction')
saveCSV(events_trafficConditions, 'trafficConditions')
