# On several occassions we encounter nested data structures. Here we looking
# into various methods to simply access the required data from such nested
# structures.🔢

#Sorting data structures in python  
"""we can sort and sorted functions to sort given data structures
sort() does not return the new data structure unlike sorted()
we can use sort() with lists only"""

voters_list = [
    ["Elon musk", "M", 30],
    ["Steve Jobs", "M", 28],
    ["Isha", "F", 1],
    ["Aryabhat", "M", 70],
    ["Vikram Batra", "M", 30]
    ]

for voter in voters_list:
    n = voter[0],
    gender = lambda g: "Male" if g == "M" else "Female"
    age = lambda a: str(a*12)+" months old" if a <= 1 else str(a)+" years old"
    
    print(f"{voter[0]} is {gender(voter[1])} and {age(voter[2])} ")
  

age_sort = lambda ag: ag[2]
sorted_voters_list = sorted(voters_list, key=age_sort)
for svl in sorted_voters_list:
    print(svl)


voters_list.sort(key=age_sort)
for sv in voters_list:
    print(sv)




