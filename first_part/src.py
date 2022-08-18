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


exercise_one()

