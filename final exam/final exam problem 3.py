import pylab
import random

#Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    
    for i in xrange(CURRENTRABBITPOP):
        p_rabbit_reproduction = 1.0 - (CURRENTRABBITPOP / float(MAXRABBITPOP))
        if random.random() <= p_rabbit_reproduction and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1

def foxGrowth():
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    global CURRENTFOXPOP

    for i in xrange(CURRENTFOXPOP):
        p_fox_eats_rabbit = CURRENTRABBITPOP/float(MAXRABBITPOP)
        if random.random() <= p_fox_eats_rabbit and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() <= 1/3.0:
                CURRENTFOXPOP += 1
        else:
            if random.random() <= 9/10.0 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1

def runSimulation(numSteps):
    rabbit_population = []
    fox_population = []
    for i in xrange(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_population.append(CURRENTRABBITPOP)
        fox_population.append(CURRENTFOXPOP)
    return (rabbit_population, fox_population)


(r, f) = runSimulation(200)
pylab.figure(1)
pylab.plot(r, 'b.')
pylab.plot(f, 'r.')
coeff = pylab.polyfit(range(len(f)), r, 2)
#trend = pylab.polyval(coeff, range(len(r)))
x_vals = pylab.array(range(len(f)))
a, b, c = pylab.polyfit(x_vals, f, 2)
est_yvals = a*x_vals**2 + b*x_vals + c
pylab.plot(est_yvals, 'b-')

pylab.show()

