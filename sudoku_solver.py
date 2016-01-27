class Box:
    # A class that defines one 3 x 3 box within the sudoku board.
    def __init__(self, input_str):
        self.grid = [[0 for x in range(3)] for x in range(3)]
        count = 0
        for i in range(0, 3):
            for p in range(0, 3):
                self.grid[i][p] = input_str[count]
                count += 1

def read_sudoku_boards(file_name, output_file):
    # This takes a text file_name with a series of puzzles, reads them one 
    # at a time into the sudoku_solver, and writes the solutions to 
    # the output_file.
    
    puzzles = open(file_name, "r")
    solved_puzzles = open(output_file, "w")
    count = 0
    # The loop continues until the end of file_name.txt.
    while len(puzzles.read(8)) > 0:
        count += 1
        # The variable board is a contiguous string of all the numbers
        # on the board, read in one row at a time.
        board = ""
        for i in range(0, 9):
            board += puzzles.read(9)
            puzzles.read(1)
        solved_board = sudoku_solver(board)
        
        # Writes the solved puzzle to the output_file.
        solved_puzzles.write("Grid " + str(count) + ":\n")
        for i in range(0, 9):
            solved_puzzles.write(solved_board[:9] + "\n")
            solved_board = solved_board[9:]
    puzzles.close()
    solved_puzzles.close()
        
def sudoku_solver(input_board):
    # This function takes in a sudoku board as one string, each row attached
    # to the next. It solves it the most that it can, and returns a string
    # in the same format as the input.
    
    board = []
    board_col = []
    boxes = []
    incomplete = True
    
    for i in range(0, 9):
        board.append(input_board[:9])
        input_board = input_board[9:]
    
    for i in range(0, 9):
        column = ""
        for q in range(0, 9):
            column += board[q][i]
        board_col.append(column)
    
    # Each iteration of this while loop can be considered as a once-over of the board, 
    # using all the tricks it has to solve more numbers. It iterates until there are
    # no more empty spots, or until no more advances can be made.
    while incomplete:
        changed = False    
        # This generates the 3 x 3 boxes on the sudoku board, making a list of them all.
        for i in range(0, 3):
            col = i * 3
            new_box1 = Box(board[col][:3] + board[col + 1][:3] + board[col + 2][:3])
            boxes.append(new_box1)
            new_box2 = Box(board[col][3:6] + board[col + 1][3:6] + board[col + 2][3:6])
            boxes.append(new_box2)
            new_box3 = Box(board[col][6:] + board[col + 1][6:] + board[col + 2][6:])
            boxes.append(new_box3)
        
        # HORIZONTALS ---------------------------------------------
        # The outer loop runs through each horizontal row.
        for row in range(0, 9):
            # The inner loop runs through each square in the row.
            for square in board[row]:
                # If the tile has a number, and it's either the first or second row in the group of three.
                if square != '0' and (row + 1) % 3 != 0:
                    # Tries to find the same number in the 3rd row. 
                    # square_in_3rd is the index of the number in the row.
                    square_in_3rd = board[row - (row % 3) + 2].find(square)
                    
                    if row % 3 == 0 and square_in_3rd != -1 and board[row + 1].find(square) == -1: 
                        # The rows that have the number are the 1st and 3rd. 
                        # The 2nd row does not.
                        
                        square_in_1st = board[row].find(square)
                        
                        if square_in_1st > 3 and square_in_3rd > 3:
                                # This means the 2nd row, 1st box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 0
                                for a in board[row + 1][:3]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    changed = True
                                    board[row + 1] = replace_square(board[row + 1], square, zero_index)
    
                        elif (square_in_1st < 3 and square_in_3rd > 6) or (square_in_1st > 6 and square_in_3rd < 3):
                                # This means the 2nd row, 2nd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 3
                                for a in board[row + 1][3:6]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    changed = True
                                    board[row + 1] = replace_square(board[row + 1], square, zero_index)
                            
                        elif square_in_1st < 6 and square_in_3rd < 6:
                                # This means the 2nd row, 3rd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 6
                                for a in board[row + 1][6:]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    changed = True
                                    board[row + 1] = replace_square(board[row + 1], square, zero_index)
                        
                    elif square_in_3rd != -1 and board[row - 1].find(square) == -1:
                        # The rows that have the number are the 2nd and 3rd. 
                        # The 1st row does not.
                        
                        square_in_2nd = board[row].find(square)
                        
                        if square_in_2nd > 3 and square_in_3rd > 3:
                                # This means the 1st row, 1st box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 0
                                for a in board[row - 1][:3]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    changed = True
                                    board[row - 1] = replace_square(board[row - 1], square, zero_index)
    
                        elif (square_in_2nd < 3 and square_in_3rd > 6) or (square_in_2nd > 6 and square_in_3rd < 3):
                                # This means the 1st row, 2nd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 3
                                for a in board[row - 1][3:6]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    changed = True
                                    board[row - 1] = replace_square(board[row - 1], square, zero_index)
                            
                        elif square_in_2nd < 6 and square_in_3rd < 6:
                                # This means the 1st row, 3rd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 6
                                for a in board[row - 1][6:]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    changed = True
                                    board[row - 1] = replace_square(board[row - 1], square, zero_index)
                    
                    elif square_in_3rd == -1 and board[row - (row % 3)].find(square) != -1 and board[row - (row % 3) + 1].find(square) != -1:
                        # The rows that have the number are the 1st and 2nd. 
                        # The 3rd row does not.
                        if row % 3 == 0:
                            square_in_1st = board[row].find(square)
                            square_in_2nd = board[row + 1].find(square)
                        else:
                            square_in_1st = board[row - 1].find(square)
                            square_in_2nd = board[row].find(square)
                            
                        third_row = row - (row % 3) + 2
                        
                        if square_in_1st > 3 and square_in_2nd > 3:
                            # This means the 3rd row, 1st box needs the square.
                            zero_count = 0
                            zero_index = 0
                            count = 0
                            for a in board[third_row][:3]:
                                if a == "_":
                                    zero_count += 1
                                    zero_index = count
                                elif a == square:
                                    zero_count = 5
                                count += 1
                                
                            # If there's only one zero in that section, the square must go there!
                            if zero_count == 1:
                                changed = True
                                board[third_row] = replace_square(board[third_row], square, zero_index)
                            
                        elif (square_in_1st < 3 and square_in_2nd > 6) or (square_in_1st > 6 and square_in_2nd < 3):
                            # This means the 3rd row, 2nd box needs the square.
                            zero_count = 0
                            zero_index = 0
                            count = 3
                            for a in board[third_row][3:6]:
                                if a == "_":
                                    zero_count += 1
                                    zero_index = count
                                elif a == square:
                                    zero_count = 5
                                count += 1
                                
                            # If there's only one zero in that section, the square must go there!
                            if zero_count == 1:
                                changed = True
                                board[third_row] = replace_square(board[third_row], square, zero_index)
    
                        elif square_in_1st < 6 and square_in_2nd < 6:
                            # This means the 3rd row, 3rd box needs the square.
                            zero_count = 0
                            zero_index = 0
                            count = 6
                            for a in board[third_row][6:]:
                                if a == "_":
                                    zero_count += 1
                                    zero_index = count
                                elif a == square:
                                    zero_count = 5
                                count += 1
                            # If there's only one zero in that section, the square must go there!
                            if zero_count == 1:
                                changed = True
                                board[third_row] = replace_square(board[third_row], square, zero_index)
    
        # VERTICALS ---------------------------------------------
        for i in range(0, 9):
            column = ""
            for q in range(0, 9):
                column += board[q][i]
            board_col[i] = column
        
        # This becomes True if any empty spots, or "_"s, are found.
        incomplete = False
        
        # The outer loop runs through each vertical column.
        for col in range(0, 9):
            # The inner loop runs through each square in the column.
            for square in board_col[col]:
                edited = False
                # If the tile has a number, and it's either the first or second column in the group of three.
                if square != '0' and (col + 1) % 3 != 0:
                    # Tries to find the same number in the 3rd column. 
                    # square_in_3rd is the index of the number in the column.
                    square_in_3rd = board_col[col - (col % 3) + 2].find(square)
                    
                    if col % 3 == 0 and square_in_3rd != -1 and board_col[col + 1].find(square) == -1: 
                        # The columns that have the number are the 1st and 3rd. 
                        # The 2nd column does not.
                        
                        square_in_1st = board_col[col].find(square)
                        
                        if square_in_1st > 3 and square_in_3rd > 3:
                                # This means the 2nd column, 1st box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 0
                                for a in board_col[col + 1][:3]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    edited = True
                                    board[zero_index] = replace_square(board[zero_index], square, col + 1)
    
                        elif (square_in_1st < 3 and square_in_3rd > 6) or (square_in_1st > 6 and square_in_3rd < 3):
                                # This means the 2nd column, 2nd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 3
                                for a in board_col[col + 1][3:6]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    edited = True
                                    board[zero_index] = replace_square(board[zero_index], square, col + 1)
                            
                        elif square_in_1st < 6 and square_in_3rd < 6:
                                # This means the 2nd column, 3rd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 6
                                for a in board_col[col + 1][6:]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    edited = True
                                    board[zero_index] = replace_square(board[zero_index], square, col + 1)
                        
                    elif square_in_3rd != -1 and board[col - 1].find(square) == -1:
                        # The columns that have the number are the 2nd and 3rd. 
                        # The 1st column does not.
                        
                        square_in_2nd = board_col[col].find(square)
                        
                        if square_in_2nd > 3 and square_in_3rd > 3:
                                # This means the 1st column, 1st box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 0
                                for a in board_col[col - 1][:3]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    edited = True
                                    board[zero_index] = replace_square(board[zero_index], square, col - 1)
    
                        elif (square_in_2nd < 3 and square_in_3rd > 6) or (square_in_2nd > 6 and square_in_3rd < 3):
                                # This means the 1st column, 2nd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 3
                                for a in board_col[col - 1][3:6]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                    
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    edited = True
                                    board[zero_index] = replace_square(board[zero_index], square, col - 1)
                            
                        elif square_in_2nd < 6 and square_in_3rd < 6:
                                # This means the 1st column, 3rd box needs the square.
                                zero_count = 0
                                zero_index = 0
                                count = 6
                                for a in board_col[col - 1][6:]:
                                    if a == "_":
                                        zero_count += 1
                                        zero_index = count
                                    elif a == square:
                                        zero_count = 5
                                    count += 1
                                # If there's only one zero in that section, the square must go there!
                                if zero_count == 1:
                                    edited = True
                                    board[zero_index] = replace_square(board[zero_index], square, col - 1)
                    
                    elif square_in_3rd == -1 and board_col[col - (col % 3)].find(square) != -1 and board_col[col - (col % 3) + 1].find(square) != -1:
                        # The columns that have the number are the 1st and 2nd. 
                        # The 3rd column does not.
                        if col % 3 == 0:
                            square_in_1st = board_col[col].find(square)
                            square_in_2nd = board_col[col + 1].find(square)
                        else:
                            square_in_1st = board_col[col - 1].find(square)
                            square_in_2nd = board_col[col].find(square)
                            
                        third_col = col - (col % 3) + 2
                        
                        if square_in_1st > 3 and square_in_2nd > 3:
                            # This means the 3rd column, 1st box needs the square.
                            zero_count = 0
                            zero_index = 0
                            count = 0
                            for a in board_col[third_col][:3]:
                                if a == "_":
                                    zero_count += 1
                                    zero_index = count
                                elif a == square:
                                    zero_count = 5
                                count += 1
                                
                            # If there's only one zero in that section, the square must go there!
                            if zero_count == 1:
                                edited = True
                                board[zero_index] = replace_square(board[zero_index], square, third_col)
                            
                        elif (square_in_1st < 3 and square_in_2nd > 6) or (square_in_1st > 6 and square_in_2nd < 3):
                            # This means the 3rd column, 2nd box needs the square.
                            zero_count = 0
                            zero_index = 0
                            count = 3
                            for a in board_col[third_col][3:6]:
                                if a == "_":
                                    zero_count += 1
                                    zero_index = count
                                elif a == square:
                                    zero_count = 5
                                count += 1
                                
                            # If there's only one zero in that section, the square must go there!
                            if zero_count == 1:
                                edited = True
                                board[zero_index] = replace_square(board[zero_index], square, third_col)
    
                        elif square_in_1st < 6 and square_in_2nd < 6:
                            # This means the 3rd column, 3rd box needs the square.
                            zero_count = 0
                            zero_index = 0
                            count = 6
                            for a in board_col[third_col][6:]:
                                if a == "_":
                                    zero_count += 1
                                    zero_index = count
                                elif a == square:
                                    zero_count = 5
                                count += 1
                            # If there's only one zero in that section, the square must go there!
                            if zero_count == 1:
                                edited = True
                                board[zero_index] = replace_square(board[zero_index], square, third_col)
                else:
                    incomplete = True
                
                if edited:
                    changed = True
                    for i in range(0, 9):
                        column = ""
                        for q in range(0, 9):
                            column += board[q][i]
                        board_col[i] = column
                        
        # Just in case the puzzle is too hard, this quits if no more advances have
        # been made instead of being stuck in the while loop forever.
        if changed == False:
            incomplete = False
     
    output_str = ""
    for i in range(0, 9):
        output_str += board[i]
                    
    return output_str

def replace_square(board_row, new_square, index):
    # This replaces a single char from a string with a new one at a given index.
    
    new_str = ""
    # transfers the old string prior to index
    for char in board_row[:index]:
        new_str += char
        
    # Inserts the new char
    new_str += new_square
    
    # transfers the old string after the index
    for char in board_row[(index + 1):]:
        new_str += char
    
    return new_str
    
read_sudoku_boards("sudoku_puzzles.txt", "solved_sudoku.txt")
