def readfile(filename):
    with open(filename,"r",encoding="utf-8") as fo :
        print(fo.read())
def seek(filename):
    with open(filename,"r",encoding="utf-8") as fo :
        print(fo.seek(1))
        print(fo.read())
def write(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
def append(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)