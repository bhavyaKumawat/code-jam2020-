import heapq


cases = int(input())
for case in range(cases):
    heap = []
    jobs = int(input())
    output = [None for x in range(jobs)]
    Cameron= -1
    Jamie= -1 
    
    for job in range(jobs):
        start , end = [int(x) for x in input().split()] 
        heapq.heappush(heap , (start , end , job) )
        
    for job in range(jobs):
        start , end , index = heapq.heappop(heap)
        if start>= Cameron:
            output[index] = 'C'
            Cameron = end
        elif start>= Jamie:
            output[index] = 'J'
            Jamie = end
        else:
            print("Case #"+str(case+1)+":" ,"IMPOSSIBLE")
            break
    else:
        print( "Case #"+str(case+1)+":" , ''.join(output))