import re
def findSum(string):
    print(sum([num for num in map(int, re.sub(r'[^0-9]', ' ', string).split())]))

findSum(input('Please Input a string: '))