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
def fib_iter2(num_of_months):
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
    
    total_female = 0
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
