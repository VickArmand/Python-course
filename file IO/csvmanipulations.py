#!/usr/bin/python3
"""
This module hosts function for manipulation of csv files
"""
import csv


def read_csv(filename=""):
    with open(filename, 'r') as f:
        return list(csv.reader(f))

def read_csv_with_headers(filename="", headers=[]):
    with open(filename, "r") as f:
        obj_dict = []
        reader = csv.DictReader(f, headers)
        count = 0
        for row in reader:
            obj_dict.append({})
            for i in headers:
                obj_dict[count][i] = row[i]
            count += 1
    return obj_dict

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
    headers = ["Name", "Age", "Course"]
    write_csv("people.csv", ["John Smith", 20, "Electrical Engineering"])
    write_csv_with_headers("students.csv", {"Name":"John Smith", "Age": 20, "Course":"Electrical Engineering"}, headers)
    print(read_csv("people.csv"))
    print(read_csv_with_headers("students.csv", headers))