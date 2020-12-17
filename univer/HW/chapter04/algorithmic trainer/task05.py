sum_i = 0
sum_j = 0
total_sum = 0
for i in range(30,0,-1):
    # sum_i += i
    print(i)
    for j in range(1, 31):
        # sum_j += j
        print(j)
        sum_ij = j / i
        total_sum += sum_ij
        print(j, i, total_sum)