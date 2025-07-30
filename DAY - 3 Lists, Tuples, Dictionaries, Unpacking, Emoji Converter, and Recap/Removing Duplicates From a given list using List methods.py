Collection=[2,2,4,6,3,4,6,1]

for val in Collection:
    if Collection.count(val)>1:
        Collection.remove(val)


print(f"The List without the repeated elements is: {Collection}")