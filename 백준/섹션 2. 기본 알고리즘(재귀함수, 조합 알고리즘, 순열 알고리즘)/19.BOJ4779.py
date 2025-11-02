import sys

def recursive(line):
    length = len(line)
    
    # base case
    if length == 1:
        return line

    # recursive case
    line_first = line[:length // 3]
    line_second = line[length // 3:length * 2 // 3].replace('-', ' ')
    line_third = line[length * 2 // 3:]
    return recursive(line_first) + recursive(line_second) + recursive(line_third)

for n in sys.stdin:
    n = int(n.rstrip())
    line = '-' * (3 ** n)
    result = recursive(line)
    print(result)