import re
def findSum(string):
    return sum([num for num in map(int, re.sub(r'[^0-9]', ' ', string).split())])

sum = findSum(input('Please Input a string: '))
print(sum)