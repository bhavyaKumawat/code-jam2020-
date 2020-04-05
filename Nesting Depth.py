cases = int(input())
for case in range(cases):
    string = [int(x) for x in input()]
    resultstring = []
    
    totalopening = 0
    previous = -1
    for digit in string:
        if digit> previous:
            times = digit-totalopening
            resultstring.extend('('*times )
            totalopening+= times
            
        if digit < previous:
            times = totalopening- digit
            resultstring.extend(')'*times )
            totalopening-= times
            
        
        resultstring.append(str(digit))
        previous = digit
    resultstring.extend(')'*totalopening )
                
    print( "Case #" + str(case+1) +':', ''.join(resultstring))
    