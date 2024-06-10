
contents = 'Shila'

try:
    with open('read_only.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('No such file found.')

print('File content:', contents)


# chmod 400 file.txt - read only

# chmod 600 file.txt - read/write