# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    additionalTimeSteps = 150
    delays = [300, 150, 75, 0]
    totalPop = []
    subplot = 0

    for delay in delays:
        totalPop = simulationWithDrug2(numViruses = 100,
                                       maxPop = 1000,
                                       maxBirthProb = 0.1,
                                       clearProb = 0.05,
                                       resistances = {'guttagonol': False},
                                       mutProb = 0.005,
                                       delay = delay,
                                       additionalTimeSteps = additionalTimeSteps,
                                       numTrials = numTrials)

        subplot += 1
        pylab.subplot(2, 2, subplot)
        pylab.hist(totalPop, bins = 50)
        pylab.xlabel('virus frequency')
        pylab.ylabel('trials')
        pylab.title('delay = %s'%delay)

    pylab.tight_layout()
    pylab.show()

def simulationWithDrug2(numViruses,
                        maxPop,
                        maxBirthProb,
                        clearProb,
                        resistances,
                        mutProb,
                        delay,
                        additionalTimeSteps,
                        numTrials):
    """
    Runs simulations and plots graphs for problem 1.
    For each of numTrials trials, instantiates a patient, runs a simulation for
    number of timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for the total virus population) as a function of time.
    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # Creates a list of viruses of len(numViruses) with maxBirthProb and clearProb
    viruses = [ResistantVirus(maxBirthProb, clearProb,resistances,mutProb)] * numViruses

    finalPopulation = []
    #resistantPopulation = []

    for trial in range(numTrials):

        print 'delay %4s: trial %4s' %(delay, trial)

        patient = TreatedPatient(viruses, maxPop)

        for timeStep in range(delay):
            patient.update()
            
        patient.addPrescription('guttagonol')

        for timeStep in range(additionalTimeSteps):
            patient.update()
    
        finalPopulation.append(patient.getTotalPop())
        #resistantPopulation.append(patient.getResistPop(['guttagonol']))
            
    #totalPopAverages = [pop / numTrials for pop in totalPopulation]
    #resistantPopAverages = [pop / numTrials for pop in resistantPopulation]

    return finalPopulation






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    additionalTimeSteps = 150
    delays = [300, 150, 75, 0]
    totalPop = []
    subplot = 0

    for delay in delays:
        totalPop = simulationWithDrug3(numViruses = 100,
                                       maxPop = 1000,
                                       maxBirthProb = 0.1,
                                       clearProb = 0.05,
                                       resistances = {'guttagonol': False, 'grimpex': False},
                                       mutProb = 0.005,
                                       delay = delay,
                                       additionalTimeSteps = additionalTimeSteps,
                                       numTrials = numTrials)

        subplot += 1
        pylab.subplot(2, 2, subplot)
        pylab.hist(totalPop, bins = 50)
        pylab.xlabel('final virus frequency')
        pylab.ylabel('trials')
        pylab.title('delay = %s'%delay)

    pylab.tight_layout()
    pylab.show()


def simulationWithDrug3(numViruses,
                        maxPop,
                        maxBirthProb,
                        clearProb,
                        resistances,
                        mutProb,
                        delay,
                        additionalTimeSteps,
                        numTrials):
    """
    Runs simulations and plots graphs for problem 1.
    For each of numTrials trials, instantiates a patient, runs a simulation for
    number of timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for the total virus population) as a function of time.
    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    initialTimeSteps = 150

    # Creates a list of viruses of len(numViruses) with maxBirthProb and clearProb
    viruses = [ResistantVirus(maxBirthProb, clearProb,resistances,mutProb)] * numViruses

    finalPopulation = []
    #resistantPopulation = []

    for trial in range(numTrials):

        print 'delay %4s: trial %4s' %(delay, trial)

        patient = TreatedPatient(viruses, maxPop)

        for timeStep in range(initialTimeSteps):
            patient.update()

        patient.addPrescription('guttagonol')

        for timeStep in range(delay):
            patient.update()
            
        patient.addPrescription('grimpex')

        for timeStep in range(additionalTimeSteps):
            patient.update()
    
        finalPopulation.append(patient.getTotalPop())
        #resistantPopulation.append(patient.getResistPop(['guttagonol']))
            
    #totalPopAverages = [pop / numTrials for pop in totalPopulation]
    #resistantPopAverages = [pop / numTrials for pop in resistantPopulation]

    return finalPopulation



if __name__ == '__main__':
    simulationTwoDrugsDelayedTreatment(numTrials = 100)
    #simulationDelayedTreatment(numTrials = 100)
