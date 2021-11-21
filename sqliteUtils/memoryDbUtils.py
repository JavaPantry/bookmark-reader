# 
# DUMP in-memory database to disk fileName
# https://stackoverflow.com/questions/27474306/with-pythons-sqlite3-module-can-i-save-the-in-memory-db-to-disk-after-creating
#
# Example: 
# dumpInMemoryDbToDisk(activeMemoryConnection, ".output\MyBookmarks-sqlite-dump.db")
# arguements:
# - memoryConnection: sqlite3.Connection object associated with in-memory database; 
#                     must be in-memory database
#                     will stay active, you are responsible to close it
#                     see https://www.sqlite.org/inmemorydb.html
# - fileName: string of file name to write to
#             will be closed on function exit
#

import os
import sqlite3
from sqlite3 import Error

def dumpInMemoryDbToDisk(memoryConnection, fileName):
    try:
        # delete existing file
        if (os.path.isfile(fileName)):
            os.remove(fileName)
        # dump memoryConnection to diskConnection
        diskConnection = sqlite3.connect(fileName)
        with diskConnection:
            for line in memoryConnection.iterdump():
                if line not in ('BEGIN;', 'COMMIT;'): # let python handle the transactions
                    diskConnection.execute(line)
        # close SqlLight db
        diskConnection.commit()
        diskConnection.close()
    except Error as e:
        print(e)


def backupInMemoryDbToDisk(memoryConnection, fileName):
    try:
        # delete existing file
        if (os.path.isfile(fileName)):
            os.remove(fileName)
        # dump in-memory database to disk file
        diskConnection = sqlite3.connect(fileName)
        memoryConnection.backup(diskConnection)
        # close SqlLight db
        diskConnection.commit()
        diskConnection.close()
    except Error as e:
        print(e)

def iterdumpInMemoryDbToDisk(memoryConnection, fileName):
    try:
        # delete existing file
        # if (os.path.isfile(fileName)):
        #     os.remove(fileName)
        open(fileName, 'w').close()
        # open file and create a cursor
        with sqlite3.connect(fileName) as db:
            dbCursor = db.cursor()
            # copy all tables from memoryConnection to db
            for tableName in memoryConnection.iterdump():
                dbCursor.execute(tableName)
    except Error as e:
        print(e)

# Not working - No such method in memoryConnection 
# def dumpInMemoryDbToDisk(memoryConnection, fileName):
#     try:
#         # delete existing file
#         if (os.path.isfile(fileName)):
#             os.remove(fileName)
#         # dump in-memory database to disk file
#         with open(fileName, "w") as f:
#             # dump in-memory database to file
# No such method in memoryConnection>>>            memoryConnection.dump(f)    
#     except Error as e:
#         print(e)


        