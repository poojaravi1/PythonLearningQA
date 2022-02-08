# use for/while loop to call each row
# sort rows using without using sort function (for 1 row - ex: bubble/merge sort)

row1 = ["software", "testing", "quality", "assurance", "to"]
row2 = ["stark", "industries", "tony", "computer", "for"]
row3 = ["from", "and", "the", "an", "nest"]
row4 = ["redundancy", "thrive", "fascinating", "pleasant", "hi"]
row5 = ["hello", "world", "breaking", "dawn", "friends"]

row1.sort()
print('After sorting Row1= ', row1)
row2.sort()
print('After sorting Row2= ', row2)
row3.sort()
print('After sorting Row3= ', row3)
row4.sort()
print('After sorting Row4= ', row4)
row5.sort()
print('After sorting Row5= ', row5)
print(sep='\n')
row6 = [row1[0], row2[0], row3[0], row4[0], row5[0]]
print('1st element of each row:' , row6)
row6.sort()
print('After sorting', row6)
print('first value = ', row6[0])
print('second value = ', row6[1])
print('third value = ', row6[2])
