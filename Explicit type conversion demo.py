# Explicit Type Conversion - Users convert the data type of an object to required data type.
# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.
# Syntax : <required_datatype>(expression)

num_int = 12
num_str = "456"

print('data type of num_int is; ', type(num_int))
print('data type of num_str is; ', type(num_str))

num_str = int(num_str)
print('data type of num_str is; ', type(num_str))

num_sum = num_int + num_str
print('Sum of num_int and num_str is: ' , num_sum)
print('data type of num-sum is:', type(num_sum))
