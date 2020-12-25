# List is a complex datatype, that is order of the collection of data
# Create a list - remember the square brackets
x = ['James', 'Karlis', 45]  # Python can mix datatype unlike other language
print(f'List:{x}')  # Print the list with square brackets
print(f'Len:{len(x)}')  # Print the list as length
# Index and positioning
print(f'Zero:{x[0]}')  # Find the first item from list
print(f'Slice:{x[1:2]}')  # Slice the list, 1 is position one and slice 2 position is karlis
# How to add the items - append, insert
x.append('Bargar')  # Adds at the end
x.append('Drink')  # Adds at the end
x.insert(1, 'Dogs')  # Adds att he specific position
print(f'List:{x}')  # Print the list after added
# Removing items - remove, pop, delete
x.remove('Drink')  # Remove item from first item
print(f'List:{x}')
i = x.index('Bargar')  # Will raise an error if not found
print(f'Food:{x.pop(i)}')  # Popping the at the top as favorite one as you deleted one from the list
print(f'list:{x}')  # Checking list that favorite one is not there due to its popping before from the list.
# Deleting
i = x.index('Dogs')  # Will rise an error if not found
del x[i]  # Delete a specific item without returning it
print(f'Deleting list:{x}')  # It's literally deleting the item from the list
# Extending - Adds elemepets from another list
y = ['Peacock', 'Dogs', 'Birds']  # New items add on the list
x.extend(y)  # As additional list
print(f'List:{x}')  # Print all the elements on the list
# Sort - sort, revers
x.remove(45)  # Need to remove number to figure out the number bkz int and str value doesn't support
x.sort()  # After removing then it can be sort
print(f'Sort:{x}')  # Now this can be sort
# Opposite of sort is revers
x.reverse()  # Call to the revers function
print(f'Revers:{x}')
# Making copy or cloning
y = x.copy()  # Copies the elements into a new list
y.reverse()  # It change the reverse position
y.append('Apples')  # add the new fruit name
print(f'Original:{x}')  # Original list
print(f'New:{y}')  # New list
# Delete the whole thing
# del y # If we write such type of memory that mean every thing is destroy from the memory
# that mean you have to rebuilt entire data structure, simply can not recover it
# print(f'List:{y}') # It generate the error so we can not do
# Clearing mean only clearing all the elements from the table
x.clear()  # Most of programing need to clear rather to delete
print(f'Cleared:{x}')
print(f'Len:{len(x)}')  # That mean it exit but no item is there

# Lists can contain other list [[],[],[]]
x = []
y = [1,2,3]
z = ['Planet','Grid']
x.append(y) # X list added with y
x.insert(0,z) # Insert the list to another list
print(f'List:{x}') # Fine the list , in advance level it will save huge time saving
print(f'Len:{len(x)}') # It will fine the how many item is there
print(f'0:{x[0][0]}') # The first list it indicate planet
print(f'1:{x[1][2]}') # Since it take item list 1 and then value of the number is 3 since the positioning value is 2

# Changing Items
x = [1,2,3,4,5]  # Hold the list of the value
x[2] = 'Tesla' # It replace the positioning value
print(x) # Print it out the particular value with the item of 2 and replace with Tesla





