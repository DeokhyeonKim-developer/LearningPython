리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for file in 리스트:
    if file.split('.')[1] == 'h' or file.split('.')[1] == 'c':
        print(file)