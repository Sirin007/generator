def reverse_gen(s):
    for st in s:
        yield st[::-1]

test_list = ['abc', 'qweqwe', 'treufjfj']
"""
for i in reverse_gen(test_list):
    print(i)
"""

def file_read(path):
    with open(path, 'r', encoding='cp1251') as strings:
        for item in strings:
            yield item


path = "/Users/sirin007/Downloads/rsosh.csv"
"""
for i in file_read(path):
    print(i)
"""

from itertools import chain

for i in chain(file_read(path),reverse_gen(test_list)):
    print(i)
