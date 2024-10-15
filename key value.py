'''
The program takes a key-value pair and adds it to the dictionary. 
Problem Solution:
1. Take a key-value pair from the user and store it in separate variables.
2. Declare a dictionary and initialize it to an empty dictionary.
3. Use the update() function to add the key-value pair to the dictionary.
4. Print the final dictionary.
5. Exit.
'''
a={}
b=input("enter the key:")
c=input("enter the key:")
a.update({b:c})
print("final dict is:",a)
