# 1) Pop() Method -> Removes the element at specified index and also returns the removed element

# Example 1 - 
languages=['Java','Python','French','Ruby','C++']

for i in range(len(languages)):
    print(i,"-->",languages[i])

# Remove the element at index 2 and return the removed element
removed=languages.pop(2)
print("The removed element is =",removed)

# Updated list
for i in range(len(languages)):
    print(i,"-->",languages[i])


# -> This method takes single argument (index) and if it is not passed then default index is -1 (index of last element)
# Example 2 -
removed2=languages.pop()         
print("The removed element is =",removed2)   

# Updated list
for i in range(len(languages)):
    print(i,"-->",languages[i])

# -> If the index passed to the method is not in range then ,it throws (IndexError): pop index out of range exception.

# Example 3 - 
# passing index out of range
languages.pop(8)     #  IndexError: pop index out of range
print(languages)


# 2) remove() -> This method removes the first matching element from the list and does not return any value

# -> This method takes single argument (element) and removes it from the list
# Example 1 -
animals=['Cat','Dog','Rabbit','Snake','Tiger','Dog']

print("Indexes of elements before removing an element")
for i in range(len(animals)):
    print(i,"-->",animals[i])

animals.remove('Snake')

print("Indexes after removing an element")
for i in range(len(animals)):
    print(i,"-->",animals[i])
    
# remove() method on list having duplicates
# Example 2 -
animals.remove('Dog')
print("Indexes after removing first occurence of element:")
for i in range(len(animals)):
    print(i,"-->",animals[i])

# -> If we try to remove the element that does not exists , it throws -> ValueError: list.remove(x): x not in list exception
# Example 3 -
animals.remove('Lion')
print(animals)       