# see python functions for work with sqllight history
# google: sqllight browser history urls.last_visit_time time format
# https://programmer.help/blogs/5d5fecf4315ec.html
# google: sqllight browser history urls last_visit_time time format
#     [How to Convert Chrome Browser History Sqlite Timestamps with Osquery](https://stackoverflow.com/questions/61197346/how-to-convert-chrome-browser-history-sqlite-timestamps-with-osquery)
#     Sources: https://linuxsleuthing.blogspot.com/2011/06/decoding-google-chrome-timestamps-in.html What is the format of Chrome's timestamps?
#     SqlLight Formula: datetime(urls.last_visit_time/1000000-11644473600, 'unixepoch') last_visit_time
#     SELECT datetime(last_visit_time/1000000-11644473600, \"unixepoch\") as last_visited, url, title, visit_count FROM urls;

# https://timestamp.online/article/how-to-convert-timestamp-to-datetime-in-python
# import time
# ts = time.gmtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
# > 2021-11-14 16:46:30
# print(time.strftime("%x %X", ts))
# > 11/14/21 16:46:30
# # Iso Format
# print(time.strftime("%c", ts))
# > Sun Nov 14 16:46:30 2021
# # Unix timestamp
# print(time.strftime("%s", ts))
# > 1636904790


# 13281193241012122
# 13281196556673378
# 13281234559289212
# 13280297396852300
# 13281291177719774
# 13281289192914789
# 13281262721197284
# 13280379088079169
# 13280642051207429

import datetime
import time


def convert_timestamp(chromeTimestamp):
    #print(type(chromeTimestamp), chromeTimestamp)
    timeStamp = chromeTimestamp/1000000-11644473600
    readable = datetime.datetime.fromtimestamp(timeStamp).isoformat()
    #print(type(readable), readable)
    return readable


def convert_timestamp2nice(chromeTimestamp):
    #print(type(chromeTimestamp), chromeTimestamp)
    timeStamp = chromeTimestamp/1000000-11644473600
    readable = time.ctime(timeStamp)
    #print(type(readable), readable)
    return readable



dates = [
13281193241012122,
13281196556673378,
13281234559289212,
13280297396852300,
13281291177719774,
13281289192914789,
13281262721197284,
13280379088079169,
13280642051207429
]

readable = datetime.datetime.fromtimestamp(1636904790).isoformat()
print('Sample data datetime.fromtimestamp(1636904790) ->',readable)
readable = time.ctime(1636904790)
print('Sample data time.ctime(1636904790) ->',readable)

ts = time.gmtime()
print('time.gmtime() ->',ts)

# readable = time.ctime(1328064205120)
# print('Sample data time.ctime(1328064205120) ->',readable)

for date in dates:
    dateStr = convert_timestamp2nice(date) # convert_timestamp(date)
    print(dateStr)

# exit()
