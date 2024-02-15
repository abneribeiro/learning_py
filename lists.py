

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

#heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
#2. Add 'black panther' at the end of this list
#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
#4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros)) # 5

heros.append('black panther') # ['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']

heros.insert(3, 'black panther') # 

heros[1:3] = ['doctor strange'] # 

heros.sort() # ['black panther', 'black panther', 'captain america', 'doctor strange',

nMax = int(input("Enter the max number : "))
odd = []
for i in range(1, nMax+1):
    if i % 2 != 0:
        odd.append(i)
print(odd) # [1, 3, 5, 7, 9]

