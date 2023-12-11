import re

result = 0

with open('input.txt', 'r') as file:
  
    for line in file:
       
        matches = re.findall(r'\d', line.strip())
        number = matches[0] + matches[-1]
        result += int(number)
print(result)