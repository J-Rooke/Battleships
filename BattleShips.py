from random import randint

#welcome message to the player
print("""###############################\n
WELCOME TO CMD LINE BATTLESHIPS\n
###############################\n""")

print(input("PRESS ENTER TO CONTINUE"))

#function to print the arena to the cmd 
def print_arena(dict):
    print("   ", end=" ")
    for i in range(1, 11):
        print("{}".format(i), end ="   ")  
    for row in dict.keys():
        print("\n")
        if row < 10:
            print("{}".format(row), end ="   ")
        else:
            print("{}".format(row), end ="  ")       
        for col, value in dict[row].items():
            if value == "W":
                print("-", end="   ")   
            elif value == "S" or value == "C" or value == "D" or value == "B":
                print("X", end="   ")
            elif value == "M":
                print("M", end="   ")    


#initializing battleships_arena and hidden arena to all water (10 x 10 grid and "W" represents water)
battleships_arena = {}
battleships_arena_hidden = {}

for i in range(1, 11):
    battleships_arena[i] = {}
    battleships_arena_hidden[i] = {}
    for y in range(1, 11):
        battleships_arena[i][y] = "W" 
        battleships_arena_hidden[i][y] = "W" 



#function to generate random ships
def generate_ships(ship, num=1):
    count = num
    while count > 0:
        row = randint(1, 10)
        column = randint(1, 10)
        if battleships_arena_hidden[row][column] == "W":
            battleships_arena_hidden[row][column] = ship
            count -= 1

generate_ships("S", 3) 

print_arena(battleships_arena)
print("   ")
print_arena(battleships_arena_hidden)



    


    

