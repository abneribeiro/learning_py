
isList = [1, 2, 3, 4, 5]

isList[1] = 6 # Change the value of the second element
isList.append(6) # Add a new element to the end of the list
isList.remove(2) # Remove the second element from the list
isList.pop(2) # Remove the third element from the list
isList.insert(2, 3) # Insert a new element at the third position
isList.sort() # Sort the list
isList.reverse() # Reverse the list
isList.clear() # Remove all elements from the list
print(isList) # [1, 6, 3, 4, 5]