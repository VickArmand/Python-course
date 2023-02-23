#!/usr/bin/python3
class Father:
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 
# Mother class inherited from Family
class Mother:
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 
# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Mark"
s1.mothername = "Sonia"
s1.show_parent()
 