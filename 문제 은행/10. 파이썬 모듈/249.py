import os

with open(str(os.getcwd()) + '/rename.txt', 'w') as f:
    pass

os.rename('rename.txt', 'rename2.txt')