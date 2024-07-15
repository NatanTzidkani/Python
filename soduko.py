def create_sudoku():
    arr = [[0] * 9 for _ in range(9)]

    print("The empty sudoku is:")
    for row in arr:
        print(" ".join(map(str, row)))

    for i in range(9):
        row_input = input(f"Enter the numbers for the {i + 1} row, Enter 0 for an empty cube: ")
        arr[i] = list(map(str, row_input))

    print("The sudoku to solve is:")
    for row in arr:
        print(" ".join(map(str, row)))
    return arr


sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def check_row(arr: list, i, j):  # get arr[i][j][1][2]
    return arr[i].count(arr[i][j]) <= 1


def check_col(arr, i, j):
    for k in range(9):
        if i == k:
            continue
        if arr[i][j] == arr[k][j]:
            return False
    return True


def check_square(arr, i, j):
    for row in range(3):
        for col in range(3):
            if i == i - (i % 3) + row and j == j - (j % 3) + col:
                continue
            if arr[i - (i % 3) + row][j - (j % 3) + col] == arr[i][j]:
                return False
    return True


def check_valid(arr, i, j):
    return check_row(arr, i, j) and check_col(arr, i, j) and check_square(arr, i, j)


def try_to_solve(arr):
    index_0 = []
    for i in range(9):
        for j in range(9):
            if sudoku_puzzle[i][j] == 0:
                index_0.append(str(i) + str(j))

    i = 0
    while True:
        if i == len(index_0):
            break
        if i == -1:
            print("Invalid Sudoku")
            exit()
        a = index_0[i]
        row = int(a[0])
        col = int(a[1])
        sudoku_puzzle[row][col] += 1
        while not check_valid(sudoku_puzzle, row, col):
            sudoku_puzzle[row][col] += 1
        if sudoku_puzzle[row][col] > 9:
            sudoku_puzzle[row][col] = 0
            i -= 1
        else:
            i += 1


def main():
    try_to_solve(sudoku_puzzle)
    print("The solved sudoku is:")
    for row in sudoku_puzzle:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
