import sqlite3
from sqlite3 import Error

# connect  to SqlLight db and write urls to table
try:
    conn = sqlite3.connect('.input\History')
    print("Connected to SQLite")
    # select all urls from urls table
    # cursor = conn.execute("SELECT urls.url, urls.title, urls.visit_count, urls.typed_count, urls.last_visit_time, urls.hidden, urls.fk, urls.fk_folder, folders.title FROM urls LEFT JOIN folders ON urls.fk_folder = folders.id")

    #cursor = conn.execute("SELECT urls.id, urls.url, urls.title, urls.visit_count, urls.typed_count, datetime(last_visit_time,'unixepoch'), urls.hidden FROM urls")
    cursor = conn.execute("SELECT id, url, title, visit_count, typed_count, datetime(last_visit_time/1000000-11644473600, \"unixepoch\") as last_visited, hidden FROM urls ORDER BY visit_count DESC")
    # for row in cursor:
    #     print("ID:", row[0])
    #     print("URL:", row[1])
    #     print("Title:", row[2])
    #     print("Visit Count:", row[3])
    #     print("Typed Count:", row[4])
    #     print("Last Visit Time:", row[5])
    #     print("Hidden:", row[6])
    #     print("\n")

    # rows keys: id, url, title, visit_count, typed_count, last_visit_time, hidden
    keys = ['id', 'url', 'title', 'visit_count', 'typed_count', 'last_visit_time', 'hidden']
    max = 10
    for row in cursor:
        buffer = "{"
        # loop through keys and add row[key index] to buffer
        for key in keys:
            buffer += '"' + key + '":"' + str(row[keys.index(key)]) + '",'
        # remove last comma
        buffer = buffer[:-1]
        buffer += "}"
        print(buffer)
        max -= 1
        if max == 0:
            break
        
except Error as e:
    print("Error:", e)


print("\nGood Bye")
exit()