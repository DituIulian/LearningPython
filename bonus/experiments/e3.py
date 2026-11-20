import glob

myfiles = glob.glob("e3/*txt")


for filepath in myfiles:
    with open(filepath, "r") as filepath:
        print(filepath.read().upper())