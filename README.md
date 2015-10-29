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
