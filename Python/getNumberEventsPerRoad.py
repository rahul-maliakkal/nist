import csv
import pandas as pd

def getNumEvents(roads, events, road_name, event_type):

    # Sort roads & events by latitude, ascending, to make matching them easier
    roads_lat_asc = roads.sort(['min_lat'], ascending=[1])
    events_lat_asc = events.sort(['latitude'], ascending=[1])

    # Get the first 7000 roads & events
    roads_lat_asc_7000 = roads_lat_asc.head(1000)
    events_lat_asc_7000 = events_lat_asc.head(1000)

    for i, row in roads_lat_asc_7000.iterrows():
        min_lat = row[10]
        min_lon = row[11]
        max_lat = row[12]
        max_lon = row[13]
        if (isinstance(min_lat, (float, int)) and
            isinstance(min_lon, (float, int)) and
            isinstance(max_lat, (float, int)) and
            isinstance(max_lon, (float, int))):
            total_events = 0
            for r in events_lat_asc_7000.itertuples():
                e_lat = r[13]
                e_lon = r[14]
                if (isinstance(e_lat, (float, int)) and
                    isinstance(e_lon, (float, int))):
                    if (e_lat >= min_lat and
                        e_lat <= max_lat and
                        e_lon >= min_lon and
                        e_lon <= max_lon):
                            total_events += 1
                else:
                    continue
            roads_lat_asc_7000.set_value(i, 'num_events_' + event_type, total_events)
        else:
            roads_lat_asc_7000.set_value(i, 'num_events_' + event_type, -1)

    roads_lat_asc_7000.to_csv('../RoadsWithNumEvents/'+road_name+'_'+event_type+'.csv')


# HARDCODED FOR NOW
road_df = pd.read_csv('../nvirginiaroads.csv')
events_df = pd.read_csv('../VirginiaEvents/e_accidentsAndIncidents_va.csv')

getNumEvents(road_df, events_df, 'nvirginiaroads', 'accidentsAndIncidents')