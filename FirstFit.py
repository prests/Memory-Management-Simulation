#!/usr/bin/python3

def defragment(memoryArr):
    for i in range(len(memoryArr)):
        for j in range(0,len(memoryArr)-i-1):
            if(memoryArr[j] == '.' and memoryArr[j+1] != '.'):
                memoryArr[j], memoryArr[j+1] = memoryArr[j+1], memoryArr[j]


def main(frame, frameSize, processes, tMemoryMove, contiguous):
    memoryArr = ['.']*frameSize
    t = 0
    completed = 0
    if(contiguous):
        print("time 0ms: Simulator Started (Contiguous -- First-Fit)")
    else:
        print("time 0ms: Simulator Started (Non-Contiguous)")
    while(True):
        for i in processes:
            if(not i.done and i.arrivalTimes[i.completed] == t):
                print("time %dms: Process %s arrived (requires %d frames)" %(t, i.name, i.size))
                count = 0
                location = 0
                defragged = False
                for j in range(len(memoryArr)):
                    if(memoryArr[j] != '.'):
                        count = 0
                    else:
                        if(count == 0):
                            location = j
                        count += 1
                        if(count == i.size):
                            for k in range(len(i.size)):
                                memoryArr[location+k] = i.name
                            break
                    
                    if(j == len(memoryArr)-1):
                        if(contiguous and not defragged):
                            j = 0
                            count = 0
                            location = 0
                            defragged = True
                            defragment(memoryArr)

                            for k in processes:
                                if(not k.done):
                                    for l in range(k.completed,len(k.endTimes)):
                                        k.endTimes[l] += tMemoryMove
                                        k.arrivalTimes[l] += tMemoryMove
                        else:
                            print("HIIII")
                            count = 0
                            location = 0
                            defragged = False
                            i.completed += 1
                            if(i.completed == len(i.endTimes)):
                                completed += 1
                                i.done = True
                            print("time %dms: Cannot place process %s -- skipped!" %(t, i.name))


        for i in processes:
            if(not i.done and i.endTimes[i.completed] == t):
                print("time %dms: Process %s removed" %(t, i.name))
                for j in range(len(memoryArr)):
                    if(memoryArr[j] == i.name):
                        memoryArr[j] = '.'
                i.completed += 1          
                if(i.completed == len(i.endTimes)):
                    completed += 1
                    i.done = True

        #print(completed)

        if(completed == len(processes)):
            break
        t += 1
    
    if(contiguous):
        print("time %dms: Simulator ended (Contiguous -- First-Fit)" %(t))
    else:
        print("time %dms: Simulator ended (Non-Contiguous)" %(t))
