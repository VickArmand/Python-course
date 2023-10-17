#!/usr/bin/python3
"""
This module hosts function for manipulation of csv files
"""
import csv


def read_csv(filename=""):
    with open(filename, 'r') as f:
        list(csv.reader(f))

def write_csv(filename="", data=[]):
    with open(filename, 'w') as f:
        outputwriter = csv.writer(f, delimiter=',')
        # data must be a list containing values
        outputwriter.writerow(data)

def write_csv_with_headers(filename="", data=[], headers=[]):
    with open(filename, 'w') as f:
        outputwriter = csv.DictWriter(f, headers)
        outputwriter.writeheader()
        # data in this must be a dictionary where the headers must be the keys
        outputwriter.writerow(data)
        outputwriter.writerow(data)

if __name__ == "__main__":
    write_csv("people.csv", ["John Smith", 20, "Electrical Engineering"])
    write_csv_with_headers("students.csv", {"Name":"John Smith", "Age": 20, "Course":"Electrical Engineering"}, ["Name", "Age", "Course"])