#
# November 13, 2021
# Run in anaconda's base python3 environment
# Brave browser bookmarks file can be taken from c:\Users\Alexei\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks
# 
# - remove loop to read root folder and point recursive readFolder() to root folder bookmarkRoot
#
# November 14, 2021
# externilize readFolder() function
# Brave browser (SqlLight db) history file can be taken from c:\Users\Alexei\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History
#
import os
import json
import sqlite3
from sqlite3 import Error
from bookmarkReaderutils import *

print("Hello. Put bookmark json file in current folder\n Currently supports Brave bookmark json file format.")
print("current folder contains")
# list files in current folder
print(os.listdir())

Input = input("Enter file name (default '.input\Bookmarks'): ") or ".input\Bookmarks"
print("selected File name: ", Input)

# Read file from current folder as json
try:
    with open(Input, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
except Exception:
    print("Error: File not found")
    exit()

# Get bookmark_bar root folder
urls = []
bookmarkRoot = json_data["roots"]["bookmark_bar"]
readFolder(bookmarkRoot, urls)

# write urls to file
print("\nSaving bookmarks in .output\MyBookmarks-urls.txt ")
with open(".output\MyBookmarks-urls.txt", "w", encoding="utf-8") as f:
    for url in urls:
        f.write(url[0] + ": " + url[1] + "\n")
print("\n bookmarks Saved in .output\MyBookmarks-urls.txt ")


print("\n connect  to SqlLight db")
# connect  to SqlLight db and write urls to table
try:
    conn = sqlite3.connect('.input\History')
    print("Connected to SQLite")
    # cursor = conn.execute("SELECT urls.url, urls.title, urls.visit_count, urls.typed_count, urls.last_visit_time, urls.hidden, urls.fk, urls.fk_folder, folders.title FROM urls LEFT JOIN folders ON urls.fk_folder = folders.id")
    cursor = conn.execute("SELECT id, url, title, visit_count, typed_count, datetime(last_visit_time/1000000-11644473600, \"unixepoch\") as last_visited, hidden FROM urls ORDER BY last_visited DESC")
    
    # rows keys: id, url, title, visit_count, typed_count, last_visit_time, hidden
    keys = ['id', 'url', 'title', 'visit_count', 'typed_count', 'last_visited', 'hidden']

    # row keys:
    max = 10
    counter = 1
    for row in cursor:
        rowStr = printRow(row, keys)
        print(str(counter) + ":" + rowStr)
        counter += 1
        max -= 1
        if max == 0:
            break
except Error as e:
    print("Error:", e)


print("\nGood Bye")
exit()

# Get list of folders
# Get list of folders
            # Folders = json_data["roots"]["other"]["children"]
            # Folders = []
            # for folder in Folders:
            #     Folders.append(folder["name"])

    



