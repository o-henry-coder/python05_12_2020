matrix = [
        [1, 5, 3],
        [0, 5, 6],
        [4, 5, 0]
    ]
def get_count_row_without_zero(matrix):
    count_row_without_zero = 0

    for row in matrix:
        is_zero = False
        for cell in row:
            if cell == 0:
                is_zero = True
                break
        if is_zero == False and len(row)>0:
            count_row_without_zero+=1

    return count_row_without_zero, row[]

print(get_count_row_without_zero(matrix))