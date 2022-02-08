# Take hexadecimal value as input, determine the color and print the color name as output
# Print the color name in respective color - Week 4

import webcolors
from webcolors import rgb_to_name
import colorama
from colorama import Fore

for i in range(1, 6):
    while True:
        try:
            hex = input('Enter Hexadecimal value: ').lstrip('#')
            # print('RGB value= ', tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4)))
            value = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
            print('Decimal value is: ', value)
            # named_color = rgb_to_name(value)
            # print(named_color)

        except ValueError:
            print('Please input only hexadecimal value!')

        else:
            break

    try:
        named_color = rgb_to_name(value)
        print('Equivalent color is: ', named_color)

    except ValueError:
        print('No defined color in CSS3')
        