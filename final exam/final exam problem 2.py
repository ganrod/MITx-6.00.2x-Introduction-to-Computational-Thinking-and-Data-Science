import math

a = [0,1,2,3,4,5,6,7,8]
b = [5,10,10,10,15]
c = [0,1,2,4,6,8]
d = [6,7,11,12,13,15]
e = [9,0,0,3,3,3,6,6]

def mean(x):    
    m = 0.0
    i = len(x)
    for e in x:
        m += e    
    return m/i

def stdDev(x):
    m = mean(x)
    i = len(x)
    s = 0
    for e in x:
        s += math.pow((e-m), 2)
    return s/i

def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

'''
print 'mean = ', mean(a), ' stdDev = ', stdDev(a)
print 'mean = ', mean(b), ' stdDev = ', stdDev(b)
print 'mean = ', mean(c), ' stdDev = ', stdDev(c)
print 'mean = ', mean(d), ' stdDev = ', stdDev(d)
print 'mean = ', mean(e), ' stdDev = ', stdDev(e)
'''

print possible_variance(a)
print possible_variance(b)
print possible_variance(c)
print possible_variance(d)
print possible_variance(e)