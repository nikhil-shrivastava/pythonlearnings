#Program to fetch values of even indices of a list

# initialize your list first
nikhil = [3,5,8,2,5,8,0,2,5,6]

print('Original list is: ',nikhil)
result = []
for index, item in enumerate(nikhil):
    if (index%2==0):
        result.append(item)
    else:
        pass
print('Elements of even indexes are: ',result)