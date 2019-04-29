#!/usr/bin/python3
import sys
import copy

import process

import FirstFit
import NextFit
import NonContiguous
import BestFit

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
    processesList_copy2 = copy.deepcopy(processesList)
    processesList_copy3 = copy.deepcopy(processesList)
    FirstFit.main(frames, frameSize, processesList, tMemoryMove, True)
    NextFit.main(frames, frameSize, processesList_copy, tMemoryMove)
    BestFit.main(frames, frameSize, processesList_copy2, tMemoryMove, False)
    NonContiguous.main(frames, frameSize, processesList_copy3, tMemoryMove, False)


'''
    Parse Command Line Arguments
'''
if __name__ == "__main__":
    #Checking size of argument array
    if(len(sys.argv) < 5):
        sys.stderr.write("ERROR: Invalid number of arguments provided\n")
        sys.exit()

    #Checking number of frames
    frames = sys.argv[1]
    try:
        frames = int(frames)
    except:
        sys.stderr.write("ERROR: Invalid number of frames (not integer)\n")
        sys.exit()
    if(frames < 0):
        sys.stderr.write("ERROR: Invalid number of frames (negative number)\n")
        sys.exit()


    #Checking frame size
    frameSize = sys.argv[2]
    try:
        frameSize = int(frameSize)
    except:
        sys.stderr.write("ERROR: Invalid frame size (not integer)\n")
        sys.exit()
    if(frameSize < 0):
        sys.stderr.write("ERROR: Invalid frame size (negative number)\n")
        sys.exit()

    #Checking if input file exists
    try:
        #print(argv[3])
        inputFile = open(sys.argv[3], 'r')
    except:
        sys.stderr.write("ERROR: Input file does not exist\n")
        sys.exit()

    #Checking time provided to move memory 
    tMemoryMove = sys.argv[4]
    try:
        tMemoryMove = int(tMemoryMove)
    except:
        sys.stderr.write("ERROR: Invalid time for memory move (not integer)\n")
        sys.exit()
    if(tMemoryMove < 0):
        sys.stderr.write("ERROR: Invalid time for memory move (negative number)\n")
        sys.exit()
    
    main(frames, frameSize, inputFile, tMemoryMove)
