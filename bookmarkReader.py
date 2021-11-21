#
# November 13, 2021
# Run in anaconda's base python3 environment
# Brave  bookmarks file can be taken from c:\Users\Alexei\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks
# Chrome bookmarks file can be taken from c:\Users\Alexei\AppData\Local\Google\Chrome\User Data\Default\Bookmarks
# 
# - remove loop to read root folder and point recursive readFolder() to root folder bookmarkRoot
#
# November 14, 2021
# externilize readFolder() function
# Brave browser (SqlLight db) history file can be taken from c:\Users\Alexei\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History
#
import sys, os
import json
import sqlite3
from sqlite3 import Error
from bookmarkReaderutils import *

# import backupInMemoryDbToDisk
# sys.path.append(os.path.join(os.path.dirname(__file__), '/sqliteUtils'))
# [Import module from subfolder](https://stackoverflow.com/questions/8953844/import-module-from-subfolder)
#   - Never and ever for the sake of your own good, name the folders or files with symbols like "-" or "_".
from sqliteUtils.memoryDbUtils import *


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

print("\n open SqlLight in memory db")
# open SqlLight in memory db
try:
    memoryConnection = sqlite3.connect(":memory:")
except Error as e:
    print(e)

print("\n create table")
# create table
c = memoryConnection.cursor()
c.execute('''CREATE TABLE bookmarks(
        id integer primary key,
        url text,
        title text,
        folder text,
        parentFolder text,
        parentId integer
        )''')
print("\n table created")

print("\n inserting bookmarks")
# insert bookmarks
for url in urls:
    c.execute("INSERT INTO bookmarks VALUES (NULL, ?, ?, 'field 3', 'field 4', 'field 5')", url)
print("\n bookmarks inserted")

print("\n save changes")
# Save changes
memoryConnection.commit()


c = memoryConnection.cursor()
c.execute('''CREATE TABLE users(
        id integer primary key,
        name text,
        password text
        )''')
print("\n users table created")
c.execute("INSERT INTO users VALUES (NULL, 'Alex', 'password')")
c.execute("INSERT INTO users VALUES (NULL, 'Joe', 'password1')")
c.execute("INSERT INTO users VALUES (NULL, 'James', 'password2')")
c.execute("INSERT INTO users VALUES (NULL, 'Mary', 'password3')")
print("\n users inserted")

print("\n save changes")
# Save changes
memoryConnection.commit()


# Inspect or Visualize in memory database created using sqlite jdbc during debugging
#       https://stackoverflow.com/questions/19098903/inspect-or-visualize-in-memory-database-created-using-sqlite-jdbc-during-debug

# save Sqlite in memory db to text file
print("\n save Sqlite in memory db to file")
memoryCursor = memoryConnection.execute("SELECT * FROM bookmarks")
with open(".output\MyBookmarks-sqlite.txt", "w", encoding="utf-8") as f:
    for row in memoryCursor:
        f.write(str(row) + "\n")
print("\n Sqlite in memory db saved to '.output\MyBookmarks-sqlite.txt' file")

# save Sqlite in memory db to disk
# open new SqlLight db file
print("\n save Sqlite in memory db to disk")
try:
    fileName = ".output\MyBookmarks-sqlite.db"
    if (os.path.isfile(fileName)):
            os.remove(fileName)
    diskConnection = sqlite3.connect(fileName)
except Error as e:
    print(e)

print("\n create table")
# create table
diskCursor = diskConnection.cursor()
diskCursor.execute('''CREATE TABLE bookmarks(
        id integer primary key,
        url text,
        title text,
        folder text,
        parentFolder text,
        parentId integer
        )''')
print("\n table created")

print("\n inserting bookmarks")
# insert bookmarks
for url in urls:
    diskCursor.execute("INSERT INTO bookmarks VALUES (NULL, ?, ?, 'field 3', 'field 4', 'field 5')", url)
print("\n bookmarks inserted")

print("\n save changes")
# Save changes
diskConnection.commit()

# print("\n save Sqlite in disk db to file")
# diskCursor = diskConnection.execute("SELECT * FROM bookmarks")
# with open(".output\MyBookmarks-sqlite.txt", "w", encoding="utf-8") as f:
#     for row in diskCursor:
#         f.write(str(row) + "\n")
# print("\n Sqlite in disk db saved to '.output\MyBookmarks-sqlite.txt' file")
# print("\n close SqlLight db")


# close SqlLight db
try:
    # memoryConnection.close()
    diskConnection.close()
except Error as e:
    print(e)

# 
# Implement 3 different ways to save in-memory database to file
#

dumpInMemoryDbToDisk(memoryConnection, ".output\MyBookmarks-sqlite-dump.db")
# backupInMemoryDbToDisk(memoryConnection, ".output\MyBookmarks-sqlite-backup.db")
# iterdumpInMemoryDbToDisk(memoryConnection, ".output\MyBookmarks-sqlite-interDump.db")

# Close connection
print("\n close memoryConnection")
memoryConnection.commit()
memoryConnection.close()
print("\n Memory database Done")



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

    # close db connection
    conn.close()

except Error as e:
    print("Error:", e)
    # close db connection
    conn.close()


print("\nGood Bye")
exit()

# Get list of folders
# Get list of folders
            # Folders = json_data["roots"]["other"]["children"]
            # Folders = []
            # for folder in Folders:
            #     Folders.append(folder["name"])

    



