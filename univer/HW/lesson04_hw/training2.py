import matplotlib.pyplot as plt
def get_kmda_from_file(filename_list) :
    arr_kmda_oklad = []
    # filename = 'january.csv'
    filename_list = ['january.csv', 'february.csv', 'march.csv']
    for filename in filename_list:
        print(filename)
        with open(filename, 'r', encoding='UTF') as myfile :
            title = myfile.readline()
            for line in myfile :
                cells = line.split(';')
                new_cell = cells[2].strip('₴').replace(',', '.').replace(' ', '')
                row = [cells[0], float(new_cell)]
                arr_kmda_oklad.append(row)
    return arr_kmda_oklad


if __name__ == '__main__':
    # filename = 'january.csv'
    filename_list = ['january.csv', 'february.csv', 'march.csv']
    for filename in filename_list :
        arr_kmda_oklad = get_kmda_from_file(filename)
        with_min_salary = arr_kmda_oklad[0]
        with_max_salary = arr_kmda_oklad[1]
        whole_salary = 0
        for worker in arr_kmda_oklad:
            whole_salary +=worker[1]
            average_sal = whole_salary/8
            if worker[1] < with_min_salary[1]:
                with_min_salary = worker
            if worker[1] > with_min_salary[1]:
                with_max_salary = worker




        print(with_min_salary, filename, with_max_salary, whole_salary, average_sal)
        mini = int(with_min_salary[1])
        maxi = int(with_max_salary[1])
        whole = int(whole_salary)
        avg = int(average_sal)

        left_edges = [4270, 11793, 334707, 41838]
        heights = [100, 200, 300, 400]

        plt.bar(left_edges, heights)
        plt.title('this is table')

        plt.xlabel('this is x')
        plt.ylabel('this is y')

        plt.grid(True)

        plt.show()
