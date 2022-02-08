dict1 = {
    "row1":["software", "testing", "quality", "assurance", "to"],
    "row2":["stark", "industries", "tony", "computer", "for"],
    "row3":["from", "and", "the", "an", "nest"],
    "row4":["redundancy", "thrive", "fascinating", "pleasant", "hi"],
    "row5":["hello", "world", "breaking", "dawn", "friends"]
}

print("\n Before Sorting: ")
for x in dict1.items():
    print(x)

print("\n After Sorting: ")
for i, j in dict1.items():
    sorted_dict = {i: sorted(j)}
    print(sorted_dict)


for k in sorted_dict:
    print(sorted_dict[k])


