
with open('my_file.txt', 'w') as file:
        file.write('Hello, My name is Nganga.\n')
        file.write('Date of birth: 14/01/2003.\n')
        file.write('And I like travelling\n')


with open('my_file.txt', 'r') as file:
        print(file.read())


# File Appending
with open('my_file.txt', 'a') as file:
        file.write('but you can call me Nimo \n')
        file.write('Gen Z of course.\n')
        file.write('21 years old\n')


with open('my_file.txt', 'r') as file:
        print(file.read())