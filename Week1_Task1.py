# Dynamic data

dict1 = {'First Name': 'Pooja', 'Aadhar Number':12345678}

dict1['First Name'] = input('Enter to your first name to retrieve Aadhar number : ')

if dict1['First Name'] == 'Pooja':
    print("Your Adhar number is:", dict1['Aadhar Number'])
else:
    print('No record found')




