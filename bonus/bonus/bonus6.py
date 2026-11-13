contents = ["All members are free.",
            "The password is incorrect.",
            "The tall three is old."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)


a = ("I`m a "
     "string")
