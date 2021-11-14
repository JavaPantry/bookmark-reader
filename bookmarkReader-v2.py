#
# November 13, 2021
# Run in anaconda's base python3 environment
# Brave browser bookmarks file can be taken from c:\Users\Alexei\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks
# 
# - remove loop to read root folder and point recursive readFolder() to root folder bookmarkRoot
#
import os
import json


def readFolder(folder, level=0):
    # construct indent on level 
    indent = '\t' * level
    for child in folder["children"]:
        if "url" in child:
            # print(child["name"], ":", child["url"])
            urls.append((indent+child["name"], child["url"]))
        else:
            # print(child["name"])
            urls.append((indent + "Folder", child["name"]))
            readFolder(child, level+1)


print("Hello. Put bookmark json file in current folder\n Currently supports Brave bookmark json file format.")
print("current folder contains")
# list files in current folder
print(os.listdir())

Input = input("Enter file name (default 'Bookmarks'): ") or "Bookmarks"
print("selected File name: ", Input)

# declare json file


# Read file from current folder as json
try:
    with open(Input, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
except Exception:
    print("Error: File not found")
    exit()
# Get list of folders
Folders = json_data["roots"]["other"]["children"]
# Get list of urls
urls = []

# Get list of bookmarks
bookmarkRoot = json_data["roots"]["bookmark_bar"]
readFolder(bookmarkRoot)

# print urls
print("\nUrls:")
for url in urls:
    print(url[0], ":", url[1])

# write urls to file
with open("MyBookmarks-urls.txt", "w", encoding="utf-8") as f:
    for url in urls:
        f.write(url[0] + ": " + url[1] + "\n")

print("\nGood Bye")
exit()

# Get list of folders
Folders = []
for folder in Folders:
    Folders.append(folder["name"])
# Get list of folders
Folders = []
for folder in Folders:
    print(folder["name"])



    



