import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return 2 * random.randint(0, 49)


print genEven()