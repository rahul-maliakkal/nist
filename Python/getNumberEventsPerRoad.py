import csv
import pandas as pd

# PARAMS:
#   roads = CSV DATAFRAME road_df file
#   events = CSV DATAFRAME event_df file
#   road_name  = STRING name of roads, i.e. nvirginiaroads
#   event_type = STRING name of event type, i.e. accidentsAndIncidents
def getNumEvents(roads, events, road_name, event_type):

    # Sort roads & events by latitude, ascending, to make matching them easier
    roads_lat_asc = roads.sort(['min_lat'], ascending=[1])
    events_lat_asc = events.sort(['latitude'], ascending=[1])

    # Get the first 7000 roads & events (or whatever int you put into .head(...))
    roads_lat_asc_7000 = roads_lat_asc.head(5)
    events_lat_asc_7000 = events_lat_asc.head(5)

    # For every row (road) in our smaller roads list...
for i, row in roads_lat_asc_7000.iterrows():
    # Get the min/max lat/lon
    min_lat = row[10]   # The indicies here may not be correct anymore
    min_lon = row[11]   # To check them, run this on a small set, maybe 5 rows
    max_lat = row[12]   # and validate that max_lat == row[12], max_lon == row[13], etc.
    max_lon = row[13]   # However, my most recent check shows they are correct
    # print(row[10])    # You can use print debugging to verify
    # print(row[11])
    # print(row[12])
    # print(row[13])

    # Validate that our min/max lat/lon values are floats
    if (isinstance(min_lat, (float, int)) and isinstance(min_lon, (float, int)) and isinstance(max_lat, (float, int)) and isinstance(max_lon, (float, int))):
        # Initialize total_events for a road <-- 0
        total_events = 0
        events_jan = 0
        events_feb = 0
        events_mar = 0
        events_apr = 0
        events_may = 0
        events_jun = 0
        events_jul = 0
        events_aug = 0
        events_sep = 0
        events_oct = 0
        events_nov = 0
        events_dec = 0

        # For each event in our smaller events list...
        for r in events_lat_asc_7000.itertuples():
            # Get the event lat and lon
            e_lat = r[11]   # Again, we need to be sure latitude == r[13] in the events CSV table
            e_lon = r[12]   # However, my most recent check shows they are correct
            is_jan = r[15]
            is_feb = r[16]
            is_mar = r[17]
            is_apr = r[18]
            is_may = r[19]
            is_jun = r[20]
            is_jul = r[21]
            is_aug = r[22]
            is_sep = r[23]
            is_oct = r[24]
            is_nov = r[25]
            is_dec = r[26]


            # print(r[13])  # You can use print debugging to verify

            # Validate that the latitudes and longitudes of the events are floats
            if (isinstance(e_lat, (float, int)) and isinstance(e_lon, (float, int))):

                # If the event's lat/lon are within the road's bounding box,
                #   increment the total_events for that road
                if (e_lat >= min_lat and e_lat <= max_lat and e_lon >= min_lon and e_lon <= max_lon):
                    if is_jan > 0:
                        events_jan+=1
                    elif is_feb > 0:
                        events_feb+=1
                    elif is_mar > 0:
                        events_mar+=1
                    elif is_apr > 0:
                        events_apr+=1
                    elif is_may > 0:
                        events_may+=1
                    elif is_jun > 0:
                        events_jun+=1
                    elif is_jul > 0:
                        events_jul+=1
                    elif is_aug > 0:
                        events_aug+=1
                    elif is_sep > 0:
                        events_sep+=1
                    elif is_oct > 0:
                        events_oct+=1
                    elif is_nov > 0:
                        events_nov+=1
                    elif is_dec > 0:
                        events_dec+=1
            else:
                continue
        # Without errors, we can now set the value of road's new column `num_events_EVENT_TYPE`
        #   to be total_events
        # roads_lat_asc_7000.set_value(i, 'num_events_' + event_type, total_events)
        roads_lat_asc_7000.set_value(i, 'events_jan', events_jan)
        roads_lat_asc_7000.set_value(i, 'events_feb', events_feb)
        roads_lat_asc_7000.set_value(i, 'events_mar', events_mar)
        roads_lat_asc_7000.set_value(i, 'events_apr', events_apr)
        roads_lat_asc_7000.set_value(i, 'events_may', events_may)
        roads_lat_asc_7000.set_value(i, 'events_jun', events_jun)
        roads_lat_asc_7000.set_value(i, 'events_jul', events_jul)
        roads_lat_asc_7000.set_value(i, 'events_aug', events_aug)
        roads_lat_asc_7000.set_value(i, 'events_sep', events_sep)
        roads_lat_asc_7000.set_value(i, 'events_oct', events_oct)
        roads_lat_asc_7000.set_value(i, 'events_nov', events_nov)
        roads_lat_asc_7000.set_value(i, 'events_dec', events_dec)

    else:
        # Else we had an error validating that the lat/lon were floats
        # roads_lat_asc_7000.set_value(i, 'num_events_' + event_type, -1)
        # roads_lat_asc_7000.set_value(i, 'events_jan', -1)
        roads_lat_asc_7000.set_value(i, 'events_jan', -1)
        roads_lat_asc_7000.set_value(i, 'events_feb', -1)
        roads_lat_asc_7000.set_value(i, 'events_mar', -1)
        roads_lat_asc_7000.set_value(i, 'events_apr', -1)
        roads_lat_asc_7000.set_value(i, 'events_may', -1)
        roads_lat_asc_7000.set_value(i, 'events_jun', -1)
        roads_lat_asc_7000.set_value(i, 'events_jul', -1)
        roads_lat_asc_7000.set_value(i, 'events_aug', -1)
        roads_lat_asc_7000.set_value(i, 'events_sep', -1)
        roads_lat_asc_7000.set_value(i, 'events_oct', -1)
        roads_lat_asc_7000.set_value(i, 'events_nov', -1)
        roads_lat_asc_7000.set_value(i, 'events_dec', -1)

# Finally, save this new roads (with the `num_events_EVENT_TYPE` column) to a new CSV
#   in the folder /RoadsWithNumEvents/
roads_lat_asc_7000.to_csv('../RoadsWithNumEvents/' + road_name + '_' + event_type + '.csv')


# HARDCODED FOR NOW

# # This road can stay the same, it is the csv of roads from our virginia bounding box
# road_df = pd.read_csv('../nvirginiaroads.csv')

# # Each of these will be the cleaned VA events csv files with confirmed t stamps

# accidentsIncidents_df = pd.read_csv('../VirginiaEvents/e_accidentsAndIncidents_va.csv')
# precipitation_df = pd.read_csv('../VirginiaEvents/e_precipitation_va.csv')

# # call the function on the same road_df, but with each event_df we want to check
#             # nvirginia, # event_type_df          # name of our roads # name of event type
# getNumEvents(road_df, accidentsAndIncidents_df, 'nvirginiaroads', 'accidentsAndIncidents')
# getNumEvents(road_df, precipitation_df, 'nvirginiaroads', 'precipitation')