from collections import defaultdict
import ast

with open('config.txt', 'r') as input_file:
    lines = input_file.readlines()


# Обрабатываем каждую строку
processed_lines = []
for line in lines:
    if "dict =" in line:
        line = line.split("=", 1)[1].strip()
        processed_line = ast.literal_eval(line)
        slovar = defaultdict(set)
        for x, num in processed_line.items():
            slovar[x].add(num)

        processed_line = 'slovar bydet takim' + str(slovar)[27:][:-1]


    elif 'def' in line:
        line = line[4:]
        x = ''
        num = ''
        while " =" in line:
            x += line[0]
            line = line[1:]
        line = line[2:]
        x=x[:-1]
        while ":" in line:
            num += line[0]
            line = line[1:]
        processed_line = 'peremennaya ' + x + ' ravna ' + num 
    
    else:
        x = ''
        num = ''
        while " =" in line:
            x += line[0]
            line = line[1:]
        line = line[2:]
        x=x[:-1]
        num = line
        processed_line = 'constanta ' + x + ' ravna ' + num 


    processed_lines.append(processed_line)


with open('output.txt', 'w') as output_file:
    for processed_line in processed_lines:
        output_file.write(f'{processed_line}\n')
