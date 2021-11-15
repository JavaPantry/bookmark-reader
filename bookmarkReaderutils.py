# Print row instead of accessing row directly with index
# #rows keys: id, url, title, visit_count, typed_count, last_visit_time, hidden
# keys = ['id', 'url', 'title', 'visit_count', 'typed_count', 'last_visited', 'hidden']
# for row in cursor:
#     rowStr = printRow(row, keys)
#     print(rowStr)
#
# old code
# for row in cursor:
#     print("ID:", row[0])
#     print("URL:", row[1])
#     print("Title:", row[2])
#     print("Visit Count:", row[3])
#     print("Typed Count:", row[4])
#     print("Last Visit Time:", row[5])
#     print("Hidden:", row[6])
#     print("\n")
#
# Return string {"id":"16","url":"https://feedly.com/","title":"ZhZh","visit_count":"1330","typed_count":"0","last_visited":"2021-11-12 13:15:56","hidden":"0"}

def printRow(row, keys):
    for key in keys:
        buffer = "{"
        # loop through keys and add row[key index] to buffer
        for key in keys:
            buffer += '"' + key + '":"' + str(row[keys.index(key)]) + '",'
        # remove last comma
        buffer = buffer[:-1]
        buffer += "}"
        return buffer


def readFolder(folder, toArray, level=0):
    # construct indent on level 
    indent = '\t' * level
    for child in folder["children"]:
        if "url" in child:
            # print(child["name"], ":", child["url"])
            toArray.append((indent+child["name"], child["url"]))
        else:
            # print(child["name"])
            toArray.append((indent + "Folder", child["name"]))
            readFolder(child, toArray, level+1)

