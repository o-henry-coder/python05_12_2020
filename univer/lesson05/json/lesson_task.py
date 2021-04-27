# 1. Прочитать из файла user.json данные в dict
# 2. Отобразить количество хобби сотрудника и вывести их на екран
# 3. Сколько детей у сотрудника
# 4. Вывести имя старшего ребенка
# 5. Добавить в dict сотрудника ключ "email": jane@company.com , "phone": 123456
# и сохранить в новый файл user2.json

import json
with open('user.json', 'r') as file:
    user_file = file.read()
    user_file_dict = json.loads(user_file)
    print(user_file_dict)


print('the hobbies are ',user_file_dict["hobbies"])
print('the number of hobbies are ', len(user_file_dict["hobbies"]))

print('the number of children ', len(user_file_dict["children"]))

elder_child = user_file_dict["children"][0]["age"]
for child in user_file_dict["children"]:
    print('the age of children ',child["age"])
    if user_file_dict["children"][0]["age"] < user_file_dict["children"][1]["age"]:
        elder_child = user_file_dict["children"][1]
    else:
        elder_child = user_file_dict["children"][0]
print('elder child is: ', elder_child)

user_file_dict["email"] = 'jane@company.com'
user_file_dict["phone"] = '123456'
print('the updated info is ',user_file_dict)

with open('user2.json', 'w') as file:
    new_user = json.dumps(user_file_dict)
    file.write(new_user)
