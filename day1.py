import re

result = 0

digit_mapping = { 
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('inputDay1.txt', 'r') as file:
  
    for line in file:
       
        matches = re.findall(r'\d|(?:zero|one|two|three|four|five|six|seven|eight|nine)', line.strip())
        
        numeric_matches = [int(digit_mapping[match.lower()]) if match.lower() in digit_mapping else int(match) for match in matches]    
        result += int(str(numeric_matches[0]) + str(numeric_matches[-1]))

print(result)