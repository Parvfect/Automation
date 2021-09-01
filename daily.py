"""
Acute Chronic Workload Ratio Automater
There needs to be a minimum 30 entries in acrw.txt before it works functionally, throws error otherwise
Calculates current workload, perfect week if needed and perfect day number.
To be completed every day for making sure the athlete remains injury free
"""

import datetime

filename = "acwr.txt"
workloads = []
thresholdMax = 1.40
thresholdMin = 0.80 

def writeNewData():
    f = open(filename, 'a')

    numberOfSessions = int(input("Enter the number of sessions"))
    sessionDuration = 0
    sessionIntensities = 0
    dayWorkload = 0

    for i in range(numberOfSessions):

        sessionDuration = int(input("Enter session {} duration".format(i)))
        sessionIntensity = int(input("Enter session {} intensity".format(i)))
        dayWorkload = dayWorkload + sessionDuration * sessionIntensity

    timing = datetime.datetime.now()

    outputString = str(dayWorkload) + " {}\n".format(timing)

    f.write(outputString)

def readData():
    
    stringRead = ""
    counter = 0

    f = open(filename, 'r')
    
    for line in f:
        stringRead = line
        if stringRead != '' :
            t = stringRead.split()
            print(t)
            workloads.append(int(t[0]))


def perfect_zone_week_number():
    """ Finds the workload number of the week for perfect zone """

    workLoad = get_workload()
    
    if workLoad < thresholdMin :
        return (get_average(23))/(1 - thresholdMin)

    elif workLoad > thresholdMax :
        return (get_average(23))/(1 - thresholdMax)

    else :
        return (get_average(23))/(1 - ((thresholdMin + thresholdMax)/2))

def perfect_zone_training_day():
    """ Finds the perfect zone training day """
    workLoad = get_workload()

    if workLoad < thresholdMin :
        return (get_average(29) - get_average(6)) / (1 - thresholdMin)
    elif workLoad > thresholdMax :
        return (get_average(29) - get_average(6)) / (1 - thresholdMax)
    else :
        return (get_average(29) - get_average(6)) / (1 - ((thresholdMin + thresholdMax)/2))
    
    return perfect_zone_training_day

def get_average(days):
    """ Returns the average of the last n days """
    average = 0
    for i in range(days):
        average = average + workloads[-1-i]
    average = average / days
    return average

def get_workload():
    """ Returns the current workload """
    sevenDayAverage = 0

    for i in range(7):
        sevenDayAverage = sevenDayAverage + workloads[-1-i] 

    sevenDayAverage = sevenDayAverage / 7

    twentyEightDayAverage = 0

    for i in range(28):
        twentyEightDayAverage = twentyEightDayAverage + workloads[-1-i] 
    
    twentyEightDayAverage /= 28

    workloadNumber = sevenDayAverage / twentyEightDayAverage
    
    return workloadNumber

def checkWorkload():

    workloadNumber = get_workload()

    if workloadNumber < thresholdMin :
        print("You are in danger of undertraining {}".format(workloadNumber))

    elif workloadNumber > thresholdMax :
        print("You are in danger of overtraining {}".format(workloadNumber))

    else :
        print("Perfect zone {}".format(workloadNumber))


if __name__ == "__main__":
    
    writeNewData()
    readData()
    
    if len(workloads) < 30 :
        print("There needs to be at least 30 entries for this to work")
    
    else :
        checkWorkload()