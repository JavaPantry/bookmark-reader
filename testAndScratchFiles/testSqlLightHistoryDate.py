import sqlite3
from sqlite3 import Error
from bookmarkReaderutils import *

# connect  to SqlLight db and write urls to table
try:
    conn = sqlite3.connect('.input\History')
    print("Connected to SQLite")
    # select all urls from urls table
    # cursor = conn.execute("SELECT urls.url, urls.title, urls.visit_count, urls.typed_count, urls.last_visit_time, urls.hidden, urls.fk, urls.fk_folder, folders.title FROM urls LEFT JOIN folders ON urls.fk_folder = folders.id")

    #cursor = conn.execute("SELECT urls.id, urls.url, urls.title, urls.visit_count, urls.typed_count, datetime(last_visit_time,'unixepoch'), urls.hidden FROM urls")
    cursor = conn.execute("SELECT id, url, title, visit_count, typed_count, datetime(last_visit_time/1000000-11644473600, \"unixepoch\") as last_visited, hidden FROM urls ORDER BY visit_count DESC")

    # rows keys: id, url, title, visit_count, typed_count, last_visit_time, hidden
    keys = ['id', 'url', 'title', 'visit_count', 'typed_count', 'last_visited', 'hidden']
    max = 10
    for row in cursor:
        rowStr = printRow(row, keys)
        print(rowStr)
        max -= 1
        if max == 0:
            break
        
except Error as e:
    print("Error:", e)


print("\nGood Bye")
exit()