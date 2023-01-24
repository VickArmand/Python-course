try:
    myFile = open("mydata.txt", encoding="utf-8")
except FileNotFoundError as ex:
    print("The file is not found")
    print(ex.args)
else:
    print("File contents are :", myFile.read())
    myFile.close()
finally:
    print("Done")