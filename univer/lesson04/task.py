# with open("task.txt", "w") as file:
#
#     for value in range(6):
#         value = input('enter any number ')
#
#     file.write(n)

# def main():
#     task_file = open('task.txt', 'w')
#     task_file.write('blahblah\n')
#     task_file.write('blah5354\n')
#     task_file.write('bl454359lah\n')
#     task_file.close()
#
# main()
#
# def read():
#     task_read = open('task.txt', 'r')
#     content = task_read.read()
#     task_read.close()
#     print(content)
# read()


# test_file = open(r'C: \ Users\ temp\test.txt', 'w')

def main():
    task = open('task.txt', 'w')
    for i in range(1,11):
        task.write(str(i)+ '\n')
    task.close()

main()