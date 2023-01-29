class Fraction:
    """
    A number is represented as a fraction
    """
    def __init__(self,num,denom):
        """ num and denom are integers"""
        # assert type(num) == int and type(denom) == int,
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Returns a string representation of self"""
        return str(self.num) + "/" + str(self.denom)
    def __add__(self,other):
        """ Returns a new fraction representing the"""
        top = self.num * other.denom + self.denom*other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)
    def __sub__(self,other):
        """ Returns a new fraction representing the """
        top = self.num * other.denom - self.denom*other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns the float value of the fraction """
        return self.num / self.denom
    def inverse(self):
        """ Returns a new fraction representing """
        return Fraction (self.denom, self.num)
a = Fraction(1,4)
b = Fraction (3,4)
c = a + b
print(c)
print(Fraction.__float__(c))
print(float(b.inverse()))