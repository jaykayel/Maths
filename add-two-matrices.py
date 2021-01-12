def menu():
    print("""
    ###############################
    # Matrices Addition made easy #
    # Welcome to the menu         #
    # Please choose what type of  #
    # Matrices you want to add.   #
    # Enter the number and hit    #
    # ENTER.                      #
    ###############################
    # 0. MANUALS                  #
    ###############################
    # 1. 2x2 Matrices             #
    # 2. 3x3 Matrices             #
    # 3. 3x2 Matrices             #
    # 4. 2x3 Matrices             #
    # 5. EXIT                     #  
    ###############################
        """)
    choice = int(input("Your choice: "))
    if choice == 0:
        manuals()
    elif choice == 1:
        two()
    elif choice == 2:
        three()
    elif choice == 3:
        threebytwo()
    elif choice == 4:
        twobythree()
    elif choice == 5:
        exit()
    else:
        menu()


def manuals():

    print("The input format for tis calculations:")
    print("######################################")
    print("""
    a = row 1 column 1
    b = row 1 column 2
    c = row 2 column 1
    d = row 2 column 2
    
    x = a b
        c d
        
    The input format will be:
    Enter first Matrix: 
    a
    b
    c
    d
    Enter second Matrix:
    a
    b
    c
    d

    
    you will be asked for all numbers separately
    
    The output format will be:
    
    z = [a, b]
        [c, d]
    """)
    print("######################################")
    menu()


def two():  # 2x2
    print("""
    ###########################################
    # You have chosen to add two 2x2 matrices #
    ###########################################
    \n""")

    # asking for first matrix
    print('Enter your first Matrix: ')
    x = []
    for i in range(0, 2):
        ele = [int(input()), int(input())]
        x.append(ele)
    print('First Matrix = ', x)
    # asking for second matrix
    print('Enter your second Matrix: ')
    y = []
    for i in range(0, 2):
        ele = [int(input()), int(input())]
        y.append(ele)
    print('Second Matrix = ', y)

    result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    print('Your result = ')
    print(result[0])
    print(result[1])
    print("\n")
    menu()


def three():    # 3x3
    print("""
    ###########################################
    # You have chosen to add two 3x3 matrices #
    ###########################################
    \n""")

    print('Enter your first Matrix:')
    x = []

    for i in range(0, 3):
        ele = [int(input()), int(input()), int(input())]
        x.append(ele)

    print('First Matrix = ', x)

    print('Enter your second Matrix:')
    y = []

    for i in range(0, 3):
        ele = [int(input()), int(input()), int(input())]
        y.append(ele)

    print('Second Matrix = ', y)

    result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    print('Your result')
    print(result[0])
    print(result[1])
    print(result[2])
    print("\n")
    menu()


def threebytwo():   # 3x2
    print("""
    ###########################################
    # You have chosen to add two 2x3 matrices #
    ###########################################
    \n""")

    print('Enter your first Matrix')
    x = []
    for i in range(0, 2):
        ele = [int(input()), int(input()), int(input())]
        x.append(ele)
    print('First Matrix = ', x)
    print('Enter your second Matrix')
    y = []
    for i in range(0, 2):
        ele = [int(input()), int(input()), int(input())]
        y.append(ele)
    print('Second Matrix = ', y)

    result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    print('Your result')
    print(result[0])
    print(result[1])
    print("\n")
    menu()


def twobythree():   # 2x3
    print("""
    ###########################################
    # You have chosen to add two 3x2 matrices #
    ###########################################
    \n""")

    print('Enter your first Matrix')
    x = []
    for i in range(0, 3):
        ele = [int(input()), int(input())]
        x.append(ele)
    print('First Matrix = ', x)

    print('Enter your second Matrix')
    y = []
    for i in range(0, 3):
        ele = [int(input()), int(input())]
        y.append(ele)
    print('Second Matrix = ', y)

    result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

    print('Your result')
    print(result[0])
    print(result[1])
    print(result[2])
    menu()


menu()
