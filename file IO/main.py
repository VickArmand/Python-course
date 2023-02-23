#!/usr/bin/python3
read = __import__("fileops").readfile
seek = __import__("fileops").seek
append = __import__("fileops").append
write = __import__("fileops").write
read("sample.txt")
seek("sample.txt")
write("sample.txt", "Text to be overwritten to the file")
read("sample.txt")
append("sample.txt", "Text to be appended to the file")
read("sample.txt")
