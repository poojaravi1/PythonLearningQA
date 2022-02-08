# Implicit Type Conversion - Python automatically converts one data type to another data type. User intervention is not needed

num1_int = 10
num2_flo = 12.5

new_num = num1_int + num2_flo

print('data type of num1_int is; ', type(num1_int))
print('data type of num2_flo is; ', type(num2_flo))

print('Value of new_num is:', new_num)
print('data type of new_num is: ', type(new_num))


print("#"*50)

num_int = 12
num_str = "Love"

print('data type of num_int is; ', type(num_int))
print('data type of num_str is; ', type(num_str))

print(num_int+num_str) # TypeError: unsupported operand type(s) for +: 'int' and 'str'