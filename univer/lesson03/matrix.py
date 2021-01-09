# def input_int_value():
#     while True:
#         try:
#             value = int(input("Enter int value"))
#             break
#         except:
#             print("Not int, try again")
#     return value
#
# def get_matrix_from_console():
#     matrix = []
#     print("Enter number row")
#     mrow = input_int_value()
#     print("Enter number collumn")
#     ncol = input_int_value()
#     for i in range(mrow):
#         matrix.append([])
#         for j in range(ncol):
#             print("Enter matrix[", i,"][",j,"]=")
#             matrix[i].append(input_int_value())
#     print(matrix)
#     return matrix
#
#
# get_matrix_from_console()


a1 = []
for j in range(5):
    a2 = []
    i = 1
    i *= 10
    for i in range(1,3):
        a2.append(i)

    a1.append(a2)
print(a1)