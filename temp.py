from collections import defaultdict

import ast

line = "dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }"


if "dict =" in line:
    line = line.split("=", 1)[1].strip()
    processed_line = ast.literal_eval(line)
    slovar = defaultdict(set)
    for key, value in processed_line.items():
        slovar[key].add(value)

    print(slovar)


# if "dict" in line:
#         line = line[4:]
#         while '{' in line:
#             line = line[1:]
#         x = ''
#         num = ''
#         n = line.count(':')
        
#         for i in range(2, 10):
#             slovar[str(i)].add(x)
#     line = "dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }"
print(len("defaultdict(<class 'set'>, "))