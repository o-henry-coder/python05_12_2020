matrix = [[1, 4, 8, 9],
          [4, 5, 3, 6],
          [1, 4, 8, 9]]
# sum_matrix = 0
# sum_row_matrix = list()
# aver_row_matrix = list()
# for row in matrix :
#     sum = 0
#     for cell in row :
#         sum += cell
#     print(sum)
#     sum_matrix += sum
#     sum_row_matrix.append(sum)
#     aver_row_matrix.append(sum / len(row))
# print(sum_matrix)
# print(sum_row_matrix)
# print(aver_row_matrix)
def rows_sum() :
    sum = 0
    sum_list = []
    for row in matrix :
        for col in row :
            sum += col
        sum_list.append(sum)
        sum = 0
    print('rows sum = ', sum_list)


##Matrix19. Дана матрица размера M × N. Для каждой строки матрицы найти сумму ее элементов.
rows_sum()


#matrix.append(rows)
# for row in rows:
#     for column in columns:
#         row.append(column)
#     matrix.append(row)
#print(matrix)

# col_sum = 0
# col_sum_list = []
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         col_sum += matrix[i][0]
#     print(col_sum)


def col_sum(matrix):
    column_sum = []
    #for column in range(4):
    for column in range(len(matrix[0])):
        sum = 0
        for row in matrix:
            sum += row[column]
        column_sum.append(sum)
    return column_sum

print('column sum = ',col_sum(matrix))