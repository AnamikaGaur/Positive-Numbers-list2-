#USING LAMBDA EXPRESSIONS

#Python Program to print all positive integers in a range

#List of Numbers
list1 = [12,14,-95,3]

#Printing positive numbers using Lambda Expressions

pos_nos = list(filter(lambda x : (x > 0),list1))

print("Positive Numbers in the list:",*pos_nos)
