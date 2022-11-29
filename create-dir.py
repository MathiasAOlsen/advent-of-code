import os
os.chdir('2015')
file_exist=False
for n in range(1,26):
    dirmaker = f'day{n}'
    try:
        os.mkdir(dirmaker)
    except FileExistsError:
        print(f'{dirmaker} already exists')