# class person:
#     mouth = 1
#     hands = 2
#     legs  = 2

# Tolu = person()

# class Politician(person):
#     pass




# class Scientist(person):
#     pass

class Data:
    def __init__(self, _list):
        self.length = len(_list)
        self.unique = str(set(_list))
        self.mean = _mean(_list)


def _mean(_list):
    _count = len(_list)
    _sum   = sum(_list)
    avg    = sum(_list) / len(_list) 
    return avg