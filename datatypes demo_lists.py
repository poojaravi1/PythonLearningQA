values = [1, 2, 'Pooja', 10.5, 9]
print(values)

print(values[0])   #[1, 2, 'Pooja', 10.5, 9]
print(values[3])   #1
print(values[-1])  #10.5
print(values[1:3]) #first one is inclusive and the last one is exclusive
values.insert(3, 'Ravi')  #[1, 2, 'Pooja', 'Ravi', 10.5, 9]
print(values)
values.append('End')  #[1, 2, 'Pooja', 'Ravi', 10.5, 9, 'End']
print(values)

values[2] = 'POOJA'  #updating - [1, 2, 'POOJA', 'Ravi', 10.5, 9, 'End']
print(values)
print(len(values))
