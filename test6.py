import webcolors
from webcolors import rgb_to_name

while True:
    try:
        hex = input('Enter Hexadecimal value: ' ).lstrip('#')
        #print('RGB value= ', tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4)))
        value = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        print(value)
        #named_color = rgb_to_name(value)
        #print(named_color)

    except ValueError:
        print('Please input only hexadecimal value!')

    else:
        break

try:
    named_color = rgb_to_name(value)
    print(named_color)
except ValueError:
    print('No defined color in CSS3')


#print('RGB value= ', tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))

