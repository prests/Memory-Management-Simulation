#!/usr/bin/python3
import sys

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