def get_filename() :
    filename_list = ['jan.csv', 'febr.csv', 'mar.csv']
    # print(filename_list[1])
    # print(len(filename_list))
    for i in range(len(filename_list)) :
        filename = filename_list[i]
        get_kmda_from_file(filename


        # with open(i, 'a') as file :
        #     file.write('hello' + '\n')


print(get_filename())

# def get_kmda_from_file(filename) :
#     arr_kmda_oklad = []
#     filename_list = ['january.csv', 'february.csv', 'march.csv']
#     for i in range(len(filename_list)) :
#         filename = filename_list[i]
#         with open(filename, 'r', encoding='UTF') as myfile :
#             title = myfile.readline()
#             for line in myfile :
#                 cells = line.split(';')
#                 new_cell = cells[3].strip('₴').replace(',', '.').replace(' ', '')
#                 row = [cells[1], float(new_cell)]
#                 arr_kmda_oklad.append(row)
#             return arr_kmda_oklad
#
#
#
# if __name__ == '__main__':
#     filename_list = ['january.csv', 'february.csv', 'march.csv']
#     for i in range(len(filename_list)) :
#         filename = filename_list[i]
#         arr_kmda_oklad = get_kmda_from_file(filename)
#         with_min_salary = arr_kmda_oklad[0]
#         with_max_salary = arr_kmda_oklad[0]
#         whole_salary = 0
#         for worker in arr_kmda_oklad:
#             whole_salary +=worker[1]
#             average_sal = whole_salary/8
#             if worker[1] < with_min_salary[1]:
#                 with_min_salary = worker
#             if worker[1] > with_min_salary[1]:
#                 with_max_salary = worker
#
#
#
#
#     print(with_min_salary, with_max_salary, whole_salary, average_sal)
#
