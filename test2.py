#use for/while loop

import itertools

row1 = ["software", "testing", "quality", "assurance", "to"]
row2 = ["stark", "industries", "tony", "computer", "for"]
row3 = ["from", "and", "the", "an", "nest"]
row4 = ["redundancy", "thrive", "fascinating", "pleasant", "hi"]
row5 = ["hello", "world", "breaking", "dawn", "friends"]

zipped_lists = zip(row1, row2, row3, row4, row5)
sorted_pairs = sorted(zipped_lists)

tuples = zip(*sorted_pairs)
row1, row2, row3, row4, row5 = [list(tuple) for tuple in tuples]

#print(row1, row2, row3, row4, row5, sep='\n')
print(row1)
print(row2)

#zip_object = zip(row1.sort(), row2.sort(), row3.sort(), row4.sort(), row5.sort())

#for (p, q, r, s, t) in zip(row1, row2, row3, row4, row5):
    #print(p, q, r, s, t)










#### row1.sort()
####print(row1)
####row2.sort()
####print(row2)
####row3.sort()
####print(row3)
####row4.sort()
####print(row4)
####row5.sort()
####print(row5)  ###
###
####row6 = [row1[0], r]
####print(row6)