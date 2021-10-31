#welcome message to the player
print("""###############################\n
WELCOME TO CMD LINE BATTLESHIPS\n
###############################\n""")

print(input("PRESS ENTER TO CONTINUE\n"))

#info for how to set ships
print("")

#initializing battleships_arena to all water
battleships_arena = {}

for i in range(1, 11):
    battleships_arena[i] = {}
    for y in range(1, 11):
        battleships_arena[i][y] = 0

print(battleships_arena[5][7])

