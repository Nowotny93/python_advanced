from os import path

if path.exists('text.txt'):
    print('File found')
else:
    print('File not found')