'''import random as ran


def Dice(turn):
    if turn == 0:
        return True
    else:
        return False
    


def main():
    while True:
        play = input("To pay Enter( to quit 'q') : ")
        if play.lower() == 'q':
            break
        else:
            Turn = ran.randint( 0 , 1)
            result = Dice(Turn)
            print(f"Toss : {result}")
            

main()'''

#
'''import random as ran

Names = []

for _ in range(4):
    Input_names = str(input("Enter the name : "))
    Names.append(Input_names)

names_str = " ".join(Names) # to create clean list 
print(f"{names_str}")
    
c = ran.choice(Names)
print(f'{c} will pay the bill hahahah')'''

'''row1 = [ '⬜️ ','⬜️' , '⬜️' ]
row2 = [ '⬜️ ','⬜️' , '⬜️' ]
row3 = [ '⬜️ ','⬜️' , '⬜️' ]


map = [ row1, row2 , row2]
print(f"{row1}\n{row2}\n{row2}\n")


col = int(input("Enter the Coloum number( 1 2 3 ) : ")) -1
row = int(input("Enter the row number( 1 2 3 ) : ")) -1
val = input("Entre X or Y. > ").upper()

map[row][col] = val

                
print(f"{' '.join(row1)}\n{' '.join(row2)}\n{' '.join(row3)}\n")'''
        
# Define the rows of the grid
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

# Combine the rows into a grid
grid = [row1, row2, row3]

# Function to print the grid
def print_grid():
    print(f"{' '.join(row1)}\n{' '.join(row2)}\n{' '.join(row3)}\n")

# Function to check if the grid is fully filled
def is_filled():
    for row in grid:
        if '⬜️' in row:
            return False
    return True

# Function to check if a player has won
def check_winner():
    # Check rows
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != '⬜️':
            return row[0]  # Return the symbol ('X' or 'Y') of the winner

    # Check columns
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '⬜️':
            return grid[0][col]

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '⬜️':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '⬜️':
        return grid[0][2]

    # No winner yet
    return None

# Main game loop
print_grid()

while not is_filled():
    row = int(input("Enter the Row number (1, 2, 3): ")) - 1
    col = int(input("Enter the Column number (1, 2, 3): ")) - 1
    val = input("Enter X or Y: ").upper()

    # Update the grid with the input value if the cell is still empty
    if grid[row][col] == '⬜️':
        grid[row][col] = val
    else:
        print("This position is already filled, please try again.")
        continue

    # Print the updated grid after each move
    print_grid()

    # Check if there's a winner after every move
    winner = check_winner()
    if winner:
        print(f"Player {winner} wins!")
        break
else:
    # If the loop ends and no winner is found, it's a draw
    print("It's a draw!")
