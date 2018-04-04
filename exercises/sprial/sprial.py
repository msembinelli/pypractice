def spiral(n):
    start_row = 0
    end_row   = n - 1
    start_col = 0
    end_col   = n - 1
    counter   = 1
    result    = [[0, 0, 0] for i in range(n)]

    while start_col <= end_col and start_row <= end_row:
        for i in range(start_col, end_col + 1):
            result[start_row][i] = counter
            counter += 1
        start_row += 1
        for i in range(start_row, end_row + 1):
            result[i][end_col] = counter
            counter += 1
        end_col -= 1
        for i in range(end_col, start_col - 1, -1):
            result[end_row][i] = counter
            counter += 1
        end_row -= 1
        for i in range(end_row, start_row - 1, -1):
            result[i][start_col] = counter
            counter += 1
        start_col += 1

    return result
