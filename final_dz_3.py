from collections import defaultdict
import ast

with open('config.txt', 'r') as input_file:
    lines = input_file.readlines()


# Обрабатываем каждую строку
processed_lines = []
for line in lines:
    if "dict =" in line:
        line = line.split("=", 1)[1].strip()
        line = ast.literal_eval(line)
        slovar = []
        for x,num in line.items():
            stroka = "Peremennoi " + str(x) + " sootvetstvyet znachenie " + str(num)
            slovar.insert(1, stroka)

        processed_line = slovar


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
        if processed_line == slovar:
            for i in range(len(slovar)):
                output_file.write(f'{slovar[i]}\n')
    
        else:
            output_file.write(f'{processed_line}\n')
