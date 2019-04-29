#!/usr/bin/python3
import sys
import copy

import process

import FirstFit
import NextFit
import NonContiguous
import BestFit

def resetProcesses(processes):
    for i in processes:
        i.done = False
        i.completed = 0
        i.running = False
        i.startTime = 0

def main(frames, frameSize, inputFile, tMemoryMove):
    processesList = []
    for line in inputFile:
        if(line[len(line)-1] == '\n'):
            line = line[:len(line)-1] 
        arr = line.split(' ')
        p = process.Process()
        for i in range(len(arr)):
            if i == 0:
                p.name = arr[i]
            elif i == 1:
                p.size = int(arr[i])
            else:
                time = arr[i].split('/')
                p.arrivalTimes.append(int(time[0]))
                p.endTimes.append(int(time[1]))
        processesList.append(p)
    
    '''
    for i in processesList:
        print(i.name)
        for j in range(len(i.arrivalTimes)):
            print(i.arrivalTimes[j])
            print(i.endTimes[j])
    '''
    
    processesList_copy = copy.deepcopy(processesList)

    FirstFit.main(frames, frameSize, processesList, tMemoryMove, True)
    resetProcesses(processesList)
    NextFit.main(frames, frameSize, processesList_copy, tMemoryMove)
    resetProcesses(processesList)
    BestFit.main(frames, frameSize, processesList, tMemoryMove, False)
    resetProcesses(processesList)
    NonContiguous.main(frames, frameSize, processesList, tMemoryMove, False)


'''
    Parse Command Line Arguments
'''
if __name__ == "__main__":
    #Checking size of argument array
    if(len(sys.argv) < 5):
        print("Invalid number of arguments provided")
        sys.exit()

    #Checking number of frames
    frames = sys.argv[1]
    try:
        frames = int(frames)
    except:
        print("Invalid number of frames provided (not integer)")
        sys.exit()

    #Checking frame size
    frameSize = sys.argv[2]
    try:
        frameSize = int(frameSize)
    except:
        print("Invalid frame size provided (not integer)")
        sys.exit()

    #Checking if input file exists
    try:
        #print(argv[3])
        inputFile = open(sys.argv[3], 'r')
    except:
        print("Input file does not exist")
        sys.exit()

    #Checking time provided to move memory 
    tMemoryMove = sys.argv[4]
    try:
        tMemoryMove = int(tMemoryMove)
    except:
        print("Invalid time provided for memory move (not integer)")
        sys.exit()
    
    main(frames, frameSize, inputFile, tMemoryMove)
