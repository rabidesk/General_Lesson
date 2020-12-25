__author__ = 'Rabi'

list = [12, 34, 200, 234] # Set the list of numbers & we want to write this number to a file.

strfile = r'C:\Users\rabic\PycharmProjects\pythonProject\test.txt' # Set the path of directory
buffer = bytes(list)  # take buffer that make the list in to bytes
print(buffer) # If you print buffer in this step then you see some xff file that don't make sense just bkz of incomplete
with open(strfile, 'bw') as f: # Binary write (bw) this file in strfile.
    f.write(buffer) # Binary file is create but you can not see as human being.

print('File written reading it back') # File start to read
with open(strfile, 'br') as f: # Open the binary file
    buffer = f.read(16) # Buffer read the file maximum 16 bytes.
    print("Lenght of buffer is %d" % len(buffer)) # Print the lenght of the file as buffer hold

    for i in buffer: # Buffer loop that print out in i value.
        print(int(i))  # print method is known as cast that converting just one data type of another


