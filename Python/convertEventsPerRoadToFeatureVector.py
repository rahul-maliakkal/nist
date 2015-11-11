import csv
import pandas as pd


globalRowCounter = 0        # keeps index of new data frame


def make_new_road_vector(roads, events, road_name, event_type):

newDF = pd.DataFrame()
newDFGlobalRow = 0
# For every row (road) in our smaller roads list...
for i, row in n_roads.iterrows():
    newDFRelativeRow = 0
    r_len = row[1]
    crossing = row[2]
    service = row[3]
    traffic_signal = row[4]
    tertiary = row[5]
    residential = row[6]
    motorway_junction = row[7]
    motorway = row[8]
    min_lat = row[9]
    min_lon = row[10]
    max_lat = row[11]
    max_lon = row[12]
    m_counter = 13
    months = []
    while m_counter < 25:
        months.append(row[m_counter])
        m_counter += 1
    newDFActualRow = 0
    # Copy these features into the new dataframe 12 times
    while newDFRelativeRow <= 11:
        newDFActualRow = newDFGlobalRow + newDFRelativeRow
        newDF.set_value(newDFActualRow, 'r_len', r_len)
        newDF.set_value(newDFActualRow, 'crossing', crossing)
        newDF.set_value(newDFActualRow, 'service', service)
        newDF.set_value(newDFActualRow, 'traffic_signal', traffic_signal)
        newDF.set_value(newDFActualRow, 'tertiary', tertiary)
        newDF.set_value(newDFActualRow, 'residential', residential)
        newDF.set_value(newDFActualRow, 'motorway_junction', motorway_junction)
        newDF.set_value(newDFActualRow, 'motorway', motorway)
        newDF.set_value(newDFActualRow, 'min_lat', min_lat)
        newDF.set_value(newDFActualRow, 'min_lon', min_lon)
        newDF.set_value(newDFActualRow, 'max_lat', max_lat)
        newDF.set_value(newDFActualRow, 'max_lon', max_lon)
        newDF.set_value(newDFActualRow, 'month', newDFRelativeRow)
        newDF.set_value(newDFActualRow, 'events', months[newDFRelativeRow])
        newDFRelativeRow += 1
    newDFGlobalRow = newDFGlobalRow + 12