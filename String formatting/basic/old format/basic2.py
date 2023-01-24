# The new-style simple formatter calls by default the __format__() method of an object for its representation. If you just want to render the output of str(...) or repr(...) you can use the !s or !r conversion flags.
# In %-style you usually use %s for the string representation but there is %r for a repr(...) conversion.
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'
print('%s %r' % (Data(), Data()))
