# These methods are of course the getter for retrieving the data and the setter for changing the data. 
# According to this principle, the attributes of a class are made private to hide and protect them.
class P:
    def __init__(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
p1 = P(42)
p2 = P(4711)
p1.get_x()
p1.set_x(47)
p1.set_x(p1.get_x()+p2.get_x())
print(p1.get_x())
class P2:
    def __init__(self, x = 0):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = P2()
p1.x = 42
print(p1.x)
# A method which is used for getting a value is decorated with "@property", i.e. we put this line directly in front of the header. 
# The method which has to function as the setter is decorated with "@x.setter". If the function had been called "f", we would have to decorate it with "@f.setter".
class P3:
    def __init__(self, x):
        self.__set_x(x)
    def __get_x(self):
        return self.__x
    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x, __set_x)
class Square:
    def __init__(self, height = 12, width = 12):
        self.height = height
        self.width = width
    @property
    def height(self):
        print("Retrieving height")
        return self.__height
    @height.setter
    def height(self, val):
        # if val.isdigit():
            self.__height = val
            print("Height is {}".format(self.__height))
        # else:
            # print("Numbers allowed only")
    @property
    def width(self):
        print("Retrieving width")
        return self.__width
    @width.setter
    def width(self, val):
        # if val.isdigit():
            self.__width = val
            print("width is {}".format(self.__width))
        # else:
            # print("Numbers allowed only")
    def getArea(self):
        return int(self.__height) * int (self.__width)
sq = Square()
height = input("Enter the height")
width = input("Enter the width")
sq.height = height
sq.width = width
print(sq.getArea())
import random, math
class Warrior:
    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax
 
    def attack(self):
        # Randomly calculate the attack amount
        # random() returns a value from 0.0 to 1.0
        attkAmt = self.attkMax * (random.random() + .5)
 
        return attkAmt
 
    def block(self):
 
        # Randomly calculate how much of the attack was blocked
        blockAmt = self.blockMax * (random.random() + .5)
 
        return blockAmt
 
# The Battle class will have the capability to loop until 1 Warrior dies
# The Warriors will each get a turn to attack each turn
 
class Battle:
 
    def startFight(self, warrior1, warrior2):
 
        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
 
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
 
    # A function will receive each Warrior that will attack the other
    # Have the attack and block amounts be integers to make the results clean
    # Output the results of the fight as it goes
    # If a Warrior dies return that result to end the looping in the
    # above function
 
    # Make this method static because we don't need to use self
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
 
        warriorBBlockAmt = warriorB.block()
 
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
 
        warriorB.health = warriorB.health - damage2WarriorB
 
        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WarriorB))
 
        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))
 
        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))
 
            return "Game Over"
        else:
            return "Fight Again"
 
 
def main():
 
    # Create 2 Warriors
    paul = Warrior("Paul", 50, 20, 10)
    sam = Warrior("Sam", 50, 20, 10)
 
    # Create Battle object
    battle = Battle()
 
    # Initiate Battle
    battle.startFight(paul, sam)
 
main()


            
            
                
        