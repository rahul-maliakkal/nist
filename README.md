# nist

## To set up event csv files for virginia, do the following:

Make sure your directory is set up as follows:

nist/
 - Python/
 - VirginiaEvents/
 - events_train.csv

From Python/ run in the following order:

 1. getEventCsv.py
 2. getVAEvents.py
 3. onlyConfirmedTStamps.py

Now your VirginiaEvents/ directory should be filled with each type of event, for Virginia, with only non-null confirmed_tstamps

## What is left

The getNumberEventsPerRoad.py file needs to be adjusted to dynamically run for event event_type csv file we have.

To test it, just copy the code that does the row and event iteration to check the bounding box alone in Pandas, with both data frames loaded appropriately as well.

Ideally, just the python file itself (getNumberEventsPerRoad) will need to be run in the command line

The factors vector will just be the columns from the final csv file that we think cause the amount of events to occur.

This can be pulled out by simple iteration over the new roads + event numbers CSV file, or you can extract it into a completely new DataFrame.
