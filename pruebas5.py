import os

for folderName, subfolders, filenames in os.walk("/../Documents/"):
    print("LA carpeta actual es" + folderName)

    for subfolder in subfolders:
        print("SUBFOLDER OF" + folderName + ": " + subfolder)

    for filename in filename:
        print("FILE INSIDE" + folderName + ": " + filename)

        