# MIT open courseware 
def genSubsets1(L):
##    print('L = ', L)
    #print('smaller = ', smaller) # return an error, 'referenced before assignment' instead of 'undefined' or 'None'.
##    if len(L) < 4:
##        print('smaller = ', smaller) # same error, 'referenced before assignment'. think of namespace.
    res = []
##    i = 0
##    j = 0
##    k =0
    if len(L) == 0:
##        counter = 0 # For testing only. Counter for new = [] down below. BUT Error Message: UnboundLocalError: local variable 'counter' referenced before assignment. Different namespaces.
        
##        print('i = ', i)
        return [[]]
##    j +=1
##    print ('j = ', j)
    smaller = genSubsets1(L[:-1]) #each time, equivalent to L.pop(). Final result is a collection of subsets without the last element.
    #print('L[:-1] = ', L[:-1])
    print ('smaller contains', smaller) # 2nd recursion starts here.
##    counter = 0 # For testing only. Counter for new = [] down below. BUT counter is reset to 0 every time.
##    length = len(L)

## equivalent 1
##    for i in range(length):
##        if length == 0:
##            return [[]]
##        smaller = genSubsets(L[: (length-1])

## equivalent 2
##    L0= L1 + []
##    for i in range(length):
##        if length == 0:
##            return [[]]
##        smaller = genSubsets(L0[:(length-1)])
##        L0.pop()
##        
    
    print('L = ', L, 'at the end recursion of smaller')
    extra  = L[- 1:]
    print ('extra contains', extra)
##    k += 1
##    print('k = ', k)
    new = [] # new is reset to [] after each for loop
##    counter += 1
##    print('new = [] has been executed for ', counter, 'times')
    for small in smaller:
        new.append(small + extra) #Bing: should be [small] instead of small?
        print('small in smaller ', small, "in", smaller)
        print('new = ', new)
    storage = smaller + new # executed once only. Values of small and new in the last cycle are added. L4, S4, extra, new
    print( 'smaller + new ', storage)
    return smaller+new

#Zhang Bing's homework
def genSubsets2(L):
    res = []
    res.append([])
    length = len(L)
    L0 = L + []

    for k in range(length):
        res.append([L[-(k+1)]])
        for i in range(length):
            smaller = L0[: -(i+1)]

##            if i == 0 or i < k:
##                extra = L0[-(i+1):]
##            else:
            extra = L0[-(i+1):]

            for small in smaller:
                res.append([small] + extra) # small is a string, one element of smaller, a list. [small] is a list. extra is a list itself.
            if i == length - 1:
                print('L0 = ', L0)
                L0.pop()
    return res

def genSubsets3(L):
    res = []
    smaller = [] # Diff 1
    
    if len(L) == 0 :
        return [[]]

    smaller = genSubsets3(L[: len(L) - 1]) # the equivalent but simpler way is L[:-1]

    extra = L[-1:]
    new = [] # Diff 2
    for small in smaller:
        new.append(small + extra) #Diff 2
    print('END OF genSubsets333333333333333333')
    return smaller+new

def genSubsets4(L):
    res = []
    print('L = ', L, "BEFORE recursion")
    if len(L) == 2:
        #return smaller # Error Message: UnboundLocalError: local variable 'smaller' referenced before assignment
##        return "length of L = 3 when 'return' executed"
        return [[]]
    smaller = genSubsets4(L[:-1])
    #print('smaller = ', smaller, '\n') # '\n' did not give me a new line, because it was NOT executed. Sequence of execution jumped to somewhere else at smaller here.
##smaller =  length of L = 3 when 'return' executed 
    print('L = ', L, "AFTER recursion")

    extra = L[-1:]
    print("extra = ", extra)
    new = []
##    print('type of small is ', type(small), '\n', 'type of smaller is ', type(smaller))
    print( 'type of smaller is ', type(smaller))
    print('smaller = ', smaller)
    for small in smaller:
##        print('type of small is ', type(small), '\n', 'type of smaller is ', type(smaller))
##        print("small in smaller = ", small, " in ", smaller)
        new.append(small + extra)
        print('new = ', new)

    print('small + extra = ', small + extra)
    print('END OF genSubsets444444444444444444')
    return new
