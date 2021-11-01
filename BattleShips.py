from random import randint

#welcome message to the player
print("""###############################\n
WELCOME TO CMD LINE BATTLESHIPS\n
###############################\n""")

print(input("PRESS ENTER TO CONTINUE"))

#function to print the arena to the cmd 
def print_arena(dict):
    print("   ", end=" ")
    for i in range(1, 10):
        print("{}".format(i), end ="   ")  
    for row in dict.keys():
        print("\n")
        print("{}".format(row), end ="   ")      
        for col, value in dict[row].items():
            if value == "W":
                print("-", end="   ")   
            elif value == "S" or value == "C" or value == "D" or value == "B":
                print("X", end="   ")
            elif value == "M":
                print("M", end="   ")    
    print(" ")            


#initializing battleships_arena and hidden arena to all water (10 x 10 grid and "W" represents water)
battleships_arena = {}
battleships_arena_hidden = {}

for i in range(1, 10):
    battleships_arena[i] = {}
    battleships_arena_hidden[i] = {}
    for y in range(1, 10):
        battleships_arena[i][y] = "W" 
        battleships_arena_hidden[i][y] = "W" 



#function to generate random ships
def generate_ships(ship, num=1):
    count = num
    while count > 0:
        row = randint(1, 9)
        column = randint(1, 9)
        if battleships_arena_hidden[row][column] == "W":
            battleships_arena_hidden[row][column] = ship
            count -= 1

#generate the ships
generate_ships("C", 2)
generate_ships("S", 3)
generate_ships("D", 4)
generate_ships("B", 5)

#get row function 
def get_row():
    row = input("enter the row you wish to shoot: ")
    while int(row) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("please enter valid row")
        row = input("enter the row you wish to shoot: ")
    return row    

#get column function        
def get_column(): 
    column = input("enter the column you wish to shoot: ")   
    while int(column) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("please enter valid column")
        column = input("enter the column you wish to shoot: ")  
    return column      



#function to shoot (main part of game)
def shoot():
    cruiser_hits = 0
    submarine_hits = 0
    destroyer_hits = 0
    battleship_hits = 0
    total_hits = 0
    score = 81

    while total_hits < 14:
        row = int(get_row())
        column = int(get_column())
        if battleships_arena_hidden[row][column] == "W":
            print("MISS!")
            score -= 1
            battleships_arena_hidden[row][column] = "M"
            battleships_arena[row][column] = "M"
        elif battleships_arena_hidden[row][column] == "S":
            print("HIT!")
            battleships_arena[row][column] = "S"
            total_hits += 1
            submarine_hits += 1
            if submarine_hits == 3:
                print("YOU HAVE SUNK THE SUBMARINE!")
        elif battleships_arena_hidden[row][column] == "C":
            print("HIT!")
            battleships_arena[row][column] = "C"
            total_hits += 1
            cruiser_hits += 1
            if cruiser_hits == 2:
                print("YOU HAVE SUNK THE CRUISER!")
        elif battleships_arena_hidden[row][column] == "D":
            print("HIT")
            battleships_arena[row][column] = "D"
            total_hits += 1
            destroyer_hits += 1
            if destroyer_hits == 4:
                print("YOU HAVE SUNK THE DESTROYER!")
        elif battleships_arena_hidden[row][column] == "B":
            print("HIT!")
            battleships_arena[row][column] = "B"  
            total_hits += 1
            battleship_hits += 1
            if destroyer_hits == 5:
                print("YOU HAVE SUNK THE BATTLESHIP!") 

        print_arena(battleships_arena)          
    print("""##############\n
    YOUR SCORE IS:\n
    ##############""")             

print_arena(battleships_arena_hidden)
shoot()     
                   
        






    


    

