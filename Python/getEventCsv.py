import csv
import pandas as pd

# Extract different event_types into their own CSVs

events_train = pd.read_csv('../events_train.csv')

# Step 1: Only get Virginia (and DDOT for deviceStatus) events

def saveVAEvents(df):
	va_events = df[df['event_id'].str.contains('VDOT|VaTraffic|DDOT')]
	return va_events

va_events = saveVAEvents(events_train)

# Step 2: Find out which month each event occured in

def extractMonthToCol(df):
	df['is_jan'] = 0
	df['is_feb'] = 0
	df['is_mar'] = 0
	df['is_apr'] = 0
	df['is_may'] = 0
	df['is_jun'] = 0
	df['is_jul'] = 0
	df['is_aug'] = 0
	df['is_sep'] = 0
	df['is_oct'] = 0
	df['is_nov'] = 0
	df['is_dec'] = 0

	for i, row in df.iterrows():
		created_tstamp = row[4]
		month = created_tstamp.split('-')[1]

		print i
		if (month == "01"):
			df.set_value(i, 'is_jan', 1)
		elif (month == "02"):
			df.set_value(i, 'is_feb', 1)
		elif (month == "03"):
			df.set_value(i, 'is_mar', 1)
		elif (month == "04"):
			df.set_value(i, 'is_apr', 1)
		elif (month == "05"):
			df.set_value(i, 'is_may', 1)
		elif (month == "06"):
			df.set_value(i, 'is_jun', 1)
		elif (month == "07"):
			df.set_value(i, 'is_jul', 1)
		elif (month == "08"):
			df.set_value(i, 'is_aug', 1)
		elif (month == "09"):
			df.set_value(i, 'is_sep', 1)
		elif (month == "10"):
			df.set_value(i, 'is_oct', 1)
		elif (month == "11"):
			df.set_value(i, 'is_nov', 1)
		elif (month == "12"):
			df.set_value(i, 'is_dec', 1)

	return df

va_events = extractMonthToCol(va_events)

# Step 3: Separate each event type into it's own DF

def getRelatedDataFrame(df, etype):
	newDf = df[df['event_type'] == etype]
	return newDf

accidentsAndIncidents_df = getRelatedDataFrame(va_events, 'accidentsAndIncidents')
roadwork_df = getRelatedDataFrame(va_events, 'roadwork')
precipitation_df = getRelatedDataFrame(va_events, 'precipitation')
deviceStatus_df = getRelatedDataFrame(va_events, 'deviceStatus')
obstruction_df = getRelatedDataFrame(va_events, 'obstruction')
trafficConditions_df = getRelatedDataFrame(va_events, 'trafficConditions')

def saveCSV(df, name):
	df.to_csv('../va_' + name + '.csv')

saveCSV(accidentsAndIncidents_df, 'accidentsAndIncidents')
saveCSV(roadwork_df, 'roadwork')
saveCSV(precipitation_df, 'precipitation')
saveCSV(deviceStatus_df, 'deviceStatus')
saveCSV(obstruction_df, 'obstruction')
saveCSV(trafficConditions_df, 'trafficConditions')