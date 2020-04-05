cases = int(input())
for case in range(cases):
    size = int(input())
    A = [[int(x) for x in input().split()] for i in range(size)]
    trace = 0
    rcount =0
    ccount =0
    for x in range(size):
        trace+= A[x][x]
        row = {}
        col = {}
        for y in range(size):
            elementrow = A[x][y]
            if elementrow in row:
                rcount+=1
                break
            else:
                row[elementrow]= 0
                
        for y in range(size):
            elementcol = A[y][x]
            if elementcol in col:
                ccount+=1
                break
            else:
                col[elementcol]= 0
                
    print("Case #"+str(case+1)+":" , trace , rcount , ccount)