# SETS

Collection_Set1 = {"A","B","C","D","E","F"}
Collection_Set2 = {1,2,3,4,5,6,7,8,9}
Collection_Set3 = {100, "set 3", "c",100, False}
print(Collection_Set1, Collection_Set2)

# Adding elements to set 
Collection_Set1.add("Alphabets Set")
Collection_Set2.add("Numbers Set")
print(f"\n{Collection_Set1} , {Collection_Set2}")

#Removing Elements
## Remove Function - Error raised if element to be removed is not in set
try:
    Collection_Set1.remove("G")
except KeyError:
    print("\nElement Trying to be removed is not in set !!")

Collection_Set2.remove(5)
print(f"\n{Collection_Set1} , {Collection_Set2}")

## Discard Method - No Error is raised if element to be removed is not in set.
Collection_Set1.discard("D")

if Collection_Set2.discard("No") is None:
    print("\nNone Value is generated as given element is not in set...")

print(f"\n{Collection_Set1} , {Collection_Set2}")

##Pop - Remove element radomly from set
Collection_Set1.pop()
Collection_Set2.pop()
print(f"\n{Collection_Set1} , {Collection_Set2}")


# Methods to Join Sets
Collection_List = [1,2,3,4,"a","F","work",22.67]

## union() method [ | ]
Collection_Set_Union_Mutiple = {}
Collection_Set_Union = Collection_Set1 | Collection_Set2
Collection_Set_Union_LIST = Collection_Set1.union(Collection_List)
Collection_Set_Union_Mutiple = Collection_Set1 | Collection_Set2 | Collection_Set3 | set(Collection_List)

print(f"\nCollection_Set_Union is {Collection_Set_Union}\nCollection_Set_Union_LIST is {Collection_Set_Union_LIST}\nCollection_Set_Union_Mutiple is {Collection_Set_Union_Mutiple}\n")

##update() method
Collection_Set_Update = {"SET UPDATE:", 100}
Collection_Set_Update.update(Collection_Set2)
print(f"\n{Collection_Set_Update}\n")

## intersection() method [ & ]
Collection_Set4 = {"A","B","C",8}
Collection_Set5 = {"A","B","C",6,7,8,9}
Collection_Set_Intersection = Collection_Set4.intersection(Collection_Set5)
print(f"\n{Collection_Set_Intersection}\n Intersection using operator '&' {Collection_Set4 & Collection_Set5}\n")

Collection_Set4.intersection_update(Collection_Set5)
print(Collection_Set4)


## difference() method [ - ]
Collection_Set6 = {"A","B","C","D","E","F","G"}
Collection_Set7 = {"A","B","C",6,7,8,9}
Collection_Set_Difference = Collection_Set6.difference(Collection_Set7)
print(f"\n{Collection_Set_Difference}\n Intersection using operator '-' {Collection_Set6 - Collection_Set7}\n")

Collection_Set6.difference_update(Collection_Set7)
print(Collection_Set6)

## symmetric_difference() method [ ^ ]
Collection_Set8 = {"A","B","C","D","E","F","G"}
Collection_Set9 = {"A","B","C",6,7,8,9}
Collection_Set_Symmetric_Difference = Collection_Set8.symmetric_difference(Collection_Set9)
print(f"\n{Collection_Set_Symmetric_Difference}\n Intersection using operator '^' {Collection_Set8 ^ Collection_Set9}\n")

Collection_Set8.symmetric_difference_update(Collection_Set9)
print(Collection_Set8)



