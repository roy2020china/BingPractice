def genSubsets(L):
    length = len(L)
    result = []
    result.append([])

    #Shift from left to right, one digit per iteration
    for k in range(length):
        result.append([L[k]])

        for i in range(k + 1, length + 1) :#when using slice, the Stop Index has to be bigger than Start Index, or it returns [].
            L0 = L[k:i] #0 is a number 0 not a letter o.
            L1 = L0 + [] #make L1 a copy of L0, in stead of an alias.

            for j in range(i, length):
                L1.append(L[j])
                result.append(L1)
                L1 = L0 + [] # initialize L1 at each iteration
    return result
