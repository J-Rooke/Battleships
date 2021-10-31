#welcome message to the player
print("""###############################\n
WELCOME TO CMD LINE BATTLESHIPS\n
###############################\n""")

print(input("PRESS ENTER TO CONTINUE"))

#info for how to set ships
print("")

#initializing battleships_arena to all water (10 x 10 grid and "W" represents water)
battleships_arena = {}

for i in range(1, 11):
    battleships_arena[i] = {}
    for y in range(1, 11):
        battleships_arena[i][y] = "W"

#function to set the squares in the arena which will be your ships ("S represnts ship")
def set_ships(id, row, col):
    #add logic to ensure ships are not set randomly and correct length 
    battleships_arena[row][col] = "S"

#function to print the arena to the cmd 
def print_arena():
    print("   ", end=" ")
    for i in range(1, 11):
        print("{}".format(i), end ="   ")  
    for row in battleships_arena.keys():
        print("\n")
        if row < 10:
            print("{}".format(row), end ="   ")
        else:
            print("{}".format(row), end ="  ")       
        for col, value in battleships_arena[row].items():
            if value == "W":
                print("-", end="   ")     


print_arena()