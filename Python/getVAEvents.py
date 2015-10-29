import csv
import pandas as pd




def saveVAEvents(df, name):
	va_events = df[df['event_id'].str.contains('VDOT|VaTraffic')]
	va_events.to_csv('../VirginiaEvents/' + name + '_va.csv')

e_accidentsAndIncidents = pd.read_csv('../e_accidentsAndIncidents.csv')
e_roadwork = pd.read_csv('../e_roadwork.csv')
e_precipitation = pd.read_csv('../e_precipitation.csv')
e_deviceStatus = pd.read_csv('../e_deviceStatus.csv')
e_obstruction = pd.read_csv('../e_obstruction.csv')
e_trafficConditions = pd.read_csv('../e_trafficConditions.csv')

saveVAEvents(e_accidentsAndIncidents, 'e_accidentsAndIncidents')
saveVAEvents(e_roadwork, 'e_roadwork')
saveVAEvents(e_precipitation, 'e_precipitation')
saveVAEvents(e_deviceStatus, 'e_deviceStatus')
saveVAEvents(e_obstruction, 'e_obstruction')
saveVAEvents(e_trafficConditions, 'e_trafficConditions')
