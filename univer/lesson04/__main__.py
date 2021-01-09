def save_to_file(arr, filename = "mytext.txt"):
    with open(filename, "w") as file_write:
        for x in arr:
            file_write.write(str(x) + "\n")


def get_list_from_file(filename = "mytext.txt"):
    arr1 = []
    with open(filename, "r") as myfile:
        for line in myfile:
            arr1.append(int(line))
    return arr1


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    save_to_file(arr,"1.txt")
    arr1 = get_list_from_file("1.txt")
    print(arr1)