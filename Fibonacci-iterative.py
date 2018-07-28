    # Zhang Bing  40224272@qq.com
# MIT open courseware
# complexity of iterative fibonacci

# from textbook
def fib_iter1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n - 1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii

def fib_iter11(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_i
        return fib_ii 

# by Zhang Bing
##def fib_iter2(num_of_months, num_of_rabbits):
##    total_female= 0
##    
##    n = num_of_months // 2 + 1 # two months for each generation to become mature and pregnant. Value of num is number of generations which actually give birth to babies.
##    for i in range(1, n):
##        num_of_generations = num_of_months - 2 * i
##        num_of_mothers = num_of_rabbits / 2 # 1/2: half of the rabbit population is female.                                                                       
##        num_of_daughters = num_of_mother * num_of_generations / 2  
##        total_female += total_female
        
# by Zhang Bing
    """iterative solution for fibonacci 

    Question: What is the total number of female rabbits at the end of a given number of months, num_of_months?
    Solution:
    1. How many mums for one specific generation?
    2. How many daughters for one generation to give birth for one time? How many times of birth-giving for one specific generation? Then, do multiplicaiton. 
    Assumption 1: two months for each generation to become mature and pregnant, including the 1st generation.
    Assumption 2: One pair of rabbits always give birth to one pair of babies.
    Variable Explanation:
    n: how many generations?
    times_of_birthgiving: how many times of birth-giving for the i-th generation?
    num_of_mums_i: the number of mums for the i-th generation, in another world, the first time mothers for the i-th generation.
    total_female_i: the number of mums for the i-th generation, together with their daughters.
    """
    
def fib_iter2(num_of_months):
    
    total_pair = 0
    n = num_of_months // 2 # num_of_generations 
    
    # case 1: num_of_months <= 1
##    if num_of_months == (0 or 1):
    if num_of_months == 0 or num_of_months == 1:
        total_female = 1
        return total_female 

    # case 2: num_of_months > 1
    else:
        for i in range(1, n + 1):                                                              
            times_of_birthgiving = num_of_months - 2 * i
            num_of_mums_i = 1
            num_of_daughters = num_of_mums_i * times_of_birthgiving * 1/2 * 2  # 1/2: assumption that a half of the rabbit population is daughters.  One pair always give birth to a new pair.
            total_female_i =  num_of_mums_i + num_of_daughters
            total_female += total_female_i
        return total_female

# Zhang Bing
"""

Re-do according to the textbook.
Compare it with fib_iter1(n), copy from the textbook.
Make sure nothing wrong with the algorithm itself.
Don't understand how the scenario of rabbit population growth in essence is a Fibonacci sequence.
"""

def fib_iter3(n):
    F_i = 0
    F_ii = 1
    
    for i in range(n-1):
        print('i = ', i)
        print('F_i, F_ii = ', F_i, ' ', F_ii)
        Tmp = F_i
        F_i = F_ii
        F_ii= F_i + Tmp
    return F_ii


#Zhang Bing
"""Re-do the growth of rabbit population

1.Fibonacci numbers is the total sum for each month, not the total sum for one specific generation.
My approach:
2. determine base number of rabbits parents for each generation, assign the value to num_of_parents_i
3. determine how many times of birth-giving for each generation? Assign the value to num_of_babies_i. Then multiply them.
4. G1, the first generation.
5. num_of_generations = n // 2
6. num_of_birthgiving = 
"""

def fib_iter4(n):
    num_of_pairs = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(0, n):
            if i == 0:
                num_of_pairs = 1
            elif i == 1:
                num_of_pairs = 1
            elif i == 2:
                num_of_babies_i = n - 2
                num_of_pairs += num_of_babies_i
            else:
                num_of_parents_i = (i - 1) * 1 # '1' represents the  1st generation
                #num_of_babies_i = (n - (i + 1)) * num_of_parents_i
                num_of_babies_i = (n - (i + 1)) * num_of_parents
                # num_of_babies_i = ( n - (i + 1)) * (i - 2) * 1
                # num_of_pairs_i = num_of_parents_i + num_of_babies_i  # WRONG. num_of_parents_i was included in the total for the 2nd time.
                num_of_pairs += num_of_babies_i
                #print('number of parents_i = ', num_of_parents_i,'||', 'number of babies_i = ', num_of_babies_i)
                print('number of babies_i = ', num_of_babies_i)
    return num_of_pairs
            
            
#Zhang Bing
"""Re-do Fibonacci sequence in the case of growth of human population

1.Time for one generation to become mature is 12months/year * 18 years.
Variable, growup cycle: cycle1
2. Time for one specific generation to become pregenant
and give birth is 12 months. 10 months/pregenancy, plus anohter 2
months, so the model is more realistic. Variable, birth cycle: cycle2
3. A time
period of 2 * (cycle1 + cycle2) later, the base number of each
generation is Fibonacci sequence. A time period of 3 * (cycle1 + cycle2)
later, base number for that generation becomes bigger. Any generation
before it remains the same as G1.
This generation is  2 * (cycle1 + cycle2) / cycle2 + 2, its base number is 2 * G1. Before this generation, all their base number is the same as that of G1. 
4. Determine how many times of
birth-giving for each generation? variable: num_of_birthgivings. For G1,
or Generation 1, num_of_birthgivings = (n - (cycle1 + cycle2) * 1) //
cycle2 for G2, num_of_birthgivings = (n - (cycle1 + cycle2) * 2) //
cycle2 From G2 onward, it is a sequence of -1. G2, G3, G4, ...,Gi, ..., Gn, num_of_birthgivings = (n - (cycle1 + cycle2) * 2) //
cycle2 - ( i - 2)
Assign the value to num_of_babies_i. Then multiply
them. 4. G1, the first generation. 5. num_of_generations = n // 2 6.
num_of_birthgiving = """

def fib_iter5(n):
    num_of_pairs = 0
    num_of_babies = 0

    cycle1 = 1
    cycle2 = 1
##    cycle1 = 12 * 18
##    cycle2 = 12 * 1

    cycle = cycle1 + cycle2

##    n < cycle means G1 has no babies
    if n in range(cycle):
        if n == 0:
            num_of_pairs = 0
            return num_of_pairs
        else:
            num_of_parents = 1
            num_of_birthgivings = 0
            num_of_babies = num_of_parents * num_of_birthgivings
            num_of_pairs = num_of_parents + num_of_babies
            return num_of_pairs

##    cycle =< n < 2 * cycle means G1 has  babies. But G1's babies not yet mature enough to have their own babies.
    elif n in range(cycle, 2 * cycle):
##        for i in range(0,  n):
        num_of_birthgivings = (n - (cycle1 + cycle2) * 1) // cycle2 # For G1 only
        num_of_babies = 1 * num_of_birthgivings  # 1: the base number of G1. num_of_parents = 1
##        num_of_babies += num_of_babies_i
        num_of_parents = 1
        num_of_pairs = num_of_parents + num_of_babies
##        print('num_of_babies = ', num_of_babies, '|', 'num_of_parents = ', num_of_parents, '|', 'num_of_pairs = ', num_of_pairs )
        return num_of_pairs

##    n > 2 *  cycle means G1 has  babies. And, G1's babies have their own babies.
    else:
##        G1
        num_of_parents_G1 = 1
        num_of_birthgivings_G1 = (n - (cycle1 + cycle2) * 1) // cycle2 # For G1 only. range(0, n)
        num_of_babies = num_of_parents_G1 * num_of_birthgivings_G1

##        G2
        num_of_parents_G2 = num_of_parents_G1
        num_of_birthgivings_G2 = (n - (cycle1 + cycle2) * 2) // cycle2
        num_of_babies += num_of_parents_G2 * num_of_birthgivings_G2

##        G3 ~ Gn
        fib_i = 0
        fib_ii = 1
        for i in range(2 * cycle, n):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_i
            num_of_parents_i = fib_ii # At Start Value of  i, num_of_parents_i is the base number for G3, NOT G2, 
            num_of_birthgivings_i = num_of_birthgivings_G2 - (i - 2 * cycle) //cycle2 - 1 # Start Value of i is 0; make it start from 1.
##            num_of_birthgivings_i = (n - (cycle1 + cycle2) * 2) // cycle2 -( i - 2 * cycle)// cycle2
            # For G2 and onward. range(0, n)
## In range(2 * cycle, n), i is time/months/year. And it means one month in the case of growth of rabbit population, 10 months in growth of human population. But actually i is birth cycle.
            num_of_babies_i = num_of_parents_i * num_of_birthgivings_i  # 1: the base number of G1. num_of_parents = 1
            #num_of_pairs_i = num_of_babies_i + num_of_parents_i
            num_of_babies += num_of_babies_i
##            print('num_of_babies, end of for loop ', num_of_babies)
            #xxx = 'inside'
##            print('xxx = ', xxx, 'when inside')
##        print('xxx = ', xxx, 'at the end')
##        num_of_pairs = num_of_parents + num_of_babies # 1: the base number of G1, num_of_parents
            print('num_of_babies = ', num_of_babies)
        num_of_pairs = num_of_parents_G1 + num_of_babies
##        print('num_of_babies = ', num_of_babies)
        return num_of_pairs
    
