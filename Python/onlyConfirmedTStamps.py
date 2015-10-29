import csv
import pandas as pd


def cleanTimeStamps(df, name):
	df = df[pd.isnull(df['confirmed_tstamp']) == False]
	df.to_csv('../VirginiaEvents/' + name + '.csv')

e_accidentsAndIncidents_va = pd.read_csv('../VirginiaEvents/e_accidentsAndIncidents_va.csv')
e_roadwork_va = pd.read_csv('../VirginiaEvents/e_roadwork_va.csv')
e_precipitation_va = pd.read_csv('../VirginiaEvents/e_precipitation_va.csv')
e_deviceStatus_va = pd.read_csv('../VirginiaEvents/e_deviceStatus_va.csv')
e_obstruction_va = pd.read_csv('../VirginiaEvents/e_obstruction_va.csv')
e_trafficConditions_va = pd.read_csv('../VirginiaEvents/e_trafficConditions_va.csv')

cleanTimeStamps(e_accidentsAndIncidents_va, 'e_accidentsAndIncidents_va')
cleanTimeStamps(e_roadwork_va, 'e_roadwork_va')
cleanTimeStamps(e_precipitation_va, 'e_precipitation_va')
cleanTimeStamps(e_deviceStatus_va, 'e_deviceStatus_va')
cleanTimeStamps(e_obstruction_va, 'e_obstruction_va')
cleanTimeStamps(e_trafficConditions_va, 'e_trafficConditions_va')


