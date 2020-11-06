file = open("file.png", 'rb')\
pngHeader = '89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52'
print(file.read())
