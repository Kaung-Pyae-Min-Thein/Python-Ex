# file = open("my_file.txt")
# print(file)
# content = file.read()
# print(content)

with open("../../../my_file.txt") as file:
        content = file.read()
        print(content)
# with open("new_file.txt", mode='w') as file:
#         file.write("New Text.")
# with open("new_file.txt") as file:
#         print(file.read())
