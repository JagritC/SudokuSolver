testboard = [[0, 0, 0, 0, 5, 6, 3, 4, 0],
             [0, 6, 3, 4, 0, 0, 0, 0, 9],
             [0, 0, 5, 9, 0, 0, 0, 0, 8],
             [0, 1, 0, 6, 0, 0, 0, 0, 5],
             [0, 0, 2, 0, 4, 1, 6, 8, 0],
             [4, 5, 0, 0, 0, 0, 0, 1, 2],
             [8, 0, 0, 0, 6, 0, 0, 0, 0],
             [0, 0, 0, 8, 0, 2, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 5, 3]]


def main_solver(board):
    find = find_empty_sq(board)
    if not find:  # base case
        return True  # we're done
    else:
        row, col = find
    for i in range(1, 10):
        if is_it_valid(board, i, (row, col)):
            board[row][col] = i

            if main_solver(board):
                return True

            board[row][col] = 0

    return False


def is_it_valid(board, num, position):
    # check if num is right in row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[
            1] != i:  # check through each column part of the row and check == num,
            return False  # pos[1] makes sure we skip over boxes we already put number in

    # check if num is right in col
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:  # similar to prev loop
            return False

    # checking the 3x3 cube
    box_x = position[1] // 3
    box_y = position[0] // 3
    # box_x, and box_y, will always be the top left of the small 3x3 cubes, i.e (0,1) will be the middle col and top row cube and next line will make that happen
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True


def print_board(board):
    for col in range(len(board)):
        for i in range(len(board[0])):
            if i % 3 == 0 and i != 0:
                print(" | ", end="")

            if i != 8:
                print(str(board[col][i]) + " ", end="")
            else:
                print(str(board[col][i]))
        if col % 3 == 2 and col != 0:
            print("------------------------")


def find_empty_sq(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):  # empty square found
                return (i, j)
    return None


print_board(testboard)
print("-------------------------------")
main_solver(testboard)
print("-------------------------------")
print_board(testboard)


