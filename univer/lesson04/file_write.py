with open('lecture_task.txt', 'w') as file:
    for num in range(6):
        num = int(input('enter any number '))
        file.write(str(num)+'\n')

with open('lecture_task.txt', 'r') as file:
    task_list = []
    for line in file:
        new_num = int(line)
        task_list.append(new_num)
    print(task_list)
    print('the sum is ', sum(task_list))
    print('the average is ', sum(task_list)/len(task_list))

