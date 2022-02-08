#Take user input and identify the datatype of the input
#Make this program continue not terminate after every step

def IdentifyInput(x):
   try:
        if type(eval(x)) == int:
            print(x, 'is of type Int')
        elif type(eval(x)) == float:
            print(x, 'is of type Float')
        elif type(eval(x)) == list:
            print('is of type List ')
        elif type(eval(x)) == tuple:
            print('is a type tuple')
        elif type(eval(x)) == dict:
            print('is a type dictionary')
        elif type(eval(x)) == complex:
            print(x, 'is of type complex')  #1+2j
        elif type(eval(x)) == bool:
            print('is of type bool')
   except:
       print("is of type string")


num1 = input('Enter any data: ')
IdentifyInput(num1)