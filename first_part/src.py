from cgi import test
from email.mime import base


def exercise_one():
    for i in range(1, 101): #we use that range to have 1 and 100 as limits
        if i%3 == 0 and i%5 == 0: #here we check if it's a multiple of 3 and 5 (must be checked first cause else it will choose either 3 or five as output)
            print("threefive")
        elif i%3 == 0 : #here if it is a multiple of 3
            print("three") 
        elif i%5 == 0 : #here if it is a multiple of five
            print("five")
        else: 
            print(i)


def check(list): 
    for i in range(len(list)): 
        for j in range(len(list)): 
            if list[i] == list[j] and i != j: 
                return 0
    return 1

def exercise_two(num): 
    list = [int(x) for x in str(num)]
    leng = 2
    set = len(list)
    testlist = list
    while check(testlist) == 1 and leng != set +1:

        for i in range(len(list)): 
            newnum = 1
            base = 0
            for j in range(leng): 
                if i+j <set:    
                    newnum *= list[i + j]
                    base +=1      
            if base == leng:
                testlist.append(newnum)
        leng += 1
    
    if check(testlist) == 0:
        return False
    else: 
        return True


def calculate(list): 
    check = 0
    sum = 0
    for i in list: 
        if type(i) == int: 
            check = 1
            sum += i
    if check == 0: 
        return False
    else: 
        return sum

def anagrams(list, word): 
    result = []
    for i in list: 
        if sorted(i) == sorted(word):
            result.append(i)
    return result
