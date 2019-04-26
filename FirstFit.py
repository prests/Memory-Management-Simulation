#!/usr/bin/python3

def printMemory(frame, frameSize, memoryArr):
    print('='*frame)
    for i in range(frameSize):
        if((i%frame == 0 and i != 0) or i == frameSize-1):
            print(memoryArr[i])
        else:
            print(memoryArr[i], end='')
    print('='*frame)

def defragment(memoryArr, processes, t):
    moved = []
    '''
    for i in range(len(memoryArr)):
        if(memoryArr[i] == '.'):
            for j in range(i,len(memoryArr)):
                if(memoryArr[j] != '.'):
                    moved.append(memoryArr[j])
    '''
    for i in range(len(memoryArr)):
        for j in range(0,len(memoryArr)-i-1):
            if(memoryArr[j] == '.' and memoryArr[j+1] != '.'):
                if(memoryArr[j+1] not in moved):
                    moved.append(memoryArr[j+1])
                memoryArr[j], memoryArr[j+1] = memoryArr[j+1], memoryArr[j]
    
    formatedString = ''
    for i in range(len(moved)):
        if(i == len(moved)-1):
            formatedString += moved[i]
        else:
            formatedString += moved[i] + ", "
    
    framesMoved = 0
    for i in processes:
        if(i in moved):
            framesMoved += i.size
    print("time %dms: Defragmentation complete (moved %d frames: %s)" %(t, framesMoved, formatedString))


def main(frame, frameSize, processes, tMemoryMove, contiguous):
    memoryArr = ['.']*frameSize
    t = 0
    completed = 0
    if(contiguous):
        print("time 0ms: Simulator Started (Contiguous -- First-Fit)")
    else:
        print("time 0ms: Simulator Started (Non-Contiguous)")
    while(True):
        event = False

        for i in processes:
            if(not i.done and i.arrivalTimes[i.completed] == t):
                print("time %dms: Process %s arrived (requires %d frames)" %(t, i.name, i.size))
                count = 0
                location = 0
                defragged = False
                numDots = 0
                for j in range(len(memoryArr)):
                    if(memoryArr[j] != '.'):
                        count = 0
                        numDots += 1
                    else:
                        if(count == 0):
                            location = j
                        count += 1
                        if(count == i.size):
                            print("time %dms: Placed process %s:" %(t, i.name))
                            i.running = True
                            event = True
                            for k in range(i.size):
                                memoryArr[location+k] = i.name
                            break
                    
                    if(j == len(memoryArr)-1):
                        if(contiguous and not defragged and numDots >= i.size): #DEFRAGMENT
                            print("time %dms: Cannot place process %s -- starting defragmentation" %(t, i.name))
                            j = 0
                            count = 0
                            location = 0
                            defragged = True
                            t += tMemoryMove
                            defragment(memoryArr, processes, t)
                            for k in processes:
                                if(not k.done):
                                    for l in range(k.completed,len(k.endTimes)):
                                        k.endTimes[l] += tMemoryMove
                                        k.arrivalTimes[l] += tMemoryMove
                        else:
                            count = 0
                            location = 0
                            defragged = False
                            i.completed += 1
                            if(i.completed == len(i.endTimes)):
                                completed += 1
                                i.done = True
                            print("time %dms: Cannot place process %s -- skipped!" %(t, i.name))
                    


        for i in processes:
            if(not i.done and i.endTimes[i.completed] == t and i.running):
                print("time %dms: Process %s removed" %(t, i.name))
                for j in range(len(memoryArr)):
                    if(memoryArr[j] == i.name):
                        memoryArr[j] = '.'
                i.completed += 1          
                if(i.completed == len(i.endTimes)):
                    completed += 1
                    i.done = True
                event = True

        if(event):
            printMemory(frame, frameSize, memoryArr)
            
        if(completed == len(processes)):
            break

        t += 1
        
    
    if(contiguous):
        print("time %dms: Simulator ended (Contiguous -- First-Fit)" %(t))
    else:
        print("time %dms: Simulator ended (Non-Contiguous)" %(t))
