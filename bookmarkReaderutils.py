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

# def readFolder(folder, toArray, level=0):
#     # construct indent on level 
#     indent = '\t' * level
#     for child in folder["children"]:
#         if "url" in child:
#             # print(child["name"], ":", child["url"])
#             toArray.append((indent+child["name"], child["url"]))
#         else:
#             # print(child["name"])
#             toArray.append((indent + "Folder", child["name"]))
#             readFolder(child, level+1)

