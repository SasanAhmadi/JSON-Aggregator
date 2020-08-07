# JSON-Aggregator
From an IOT system we have gathered a log of sensor observations as a JSONL text file with the
following format:

{"date": "2019-01-01", "time": "14:09:13.010", "input": "sensor_17", "value": 56.65788628257326}
{"date": "2019-01-01", "time": "16:07:09.166", "input": "sensor_23", "value": -6.939272293750748}
{"date": "2019-01-01", "time": "12:18:39.988", "input": "sensor_103", "value": 14.45649620272106}
...

The dates in the input file are guaranteed to appear in order.

python application is a small command line tool to aggregate the data per day,
and for each day to report the median value for each sensor. The output file is in the
following format:

{"date": "2019-01-01", "input": "sensor_134", "median_value": 19.09421548912573}
{"date": "2019-01-01", "input": "sensor_121", "median_value": 12.99225035624281}
{"date": "2019-01-01", "input": "sensor_33", "median_value": -30.332243582193147}
...

The solution is designed in a way so that it can scale up to much larger
input files. Because it is not reasonable to load all data (even in parsed form) into memory at once I used file iterator over each line.


# some other change !