# In Python 3 there exists an additional conversion flag that uses the output of repr(...) but uses ascii(...) instead.
class Data(object):

    def __repr__(self):
        return 'räpr'
print('{0!r} {0!a}'.format(Data()))