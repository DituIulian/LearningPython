file_path = input("Enter file path: ").strip('"')

with open(file_path, "rb") as file:
    header = file.read(32)

print("Hex:", header.hex(" "))
print("Raw bytes:", header)