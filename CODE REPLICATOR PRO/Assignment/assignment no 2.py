'''
Title:- Write a python program to create a Tuple and perform the various
operations on Tuple
Name:- Ganesh Wagh
Roll NO:- 133
Batch:- Aids-B3
'''
a = int(input("Enter Tuple element n 1:"))
b = int(input("Enter Tuple element n 2:"))
c = int(input("Enter Tuple element n 3:"))
d = int(input("Enter Tuple element n 4:"))
e = int(input("Enter Tuple element n 5:"))
tuple1 = (a, b, c, d, e)
new_even_tuple = ()
new_odd_tuple = ()
print("CREATED TUPLE IS:", tuple1)
repeated_tuple = tuple1 * 2
print("Repeated Tuple:", repeated_tuple)
print("Length of Tuple:", len(tuple1))
print("Tuple Slice (1:4):", tuple1[1:4])
tuple2 = (60, 70, 80, 90, 100)
combined_tuple = tuple1 + tuple2
print("Concatenated Tuple1 + Tuple2:", combined_tuple)
for i in tuple1:
 if i % 2 == 0:
    new_even_tuple = new_even_tuple + (i,)
 else:
    new_odd_tuple = new_odd_tuple + (i,)
print("The even numbers in the tuple are:", new_even_tuple)
print("The odd numbers in the tuple are:", new_odd_tuple)
# *********OUTPUT********* #
'''(base) aids@aids-OptiPlex-3000:~$ python3 Ganesh Wagh4.py
Enter Tuple element n 1:8
Enter Tuple element n 2:67
Enter Tuple element n 3:3
Enter Tuple element n 4:2 
Enter Tuple element n 5:45
CREATED TUPLE IS: (8, 67, 3, 2, 45)
Repeated Tuple: (8, 67, 3, 2, 45, 8, 67, 3, 2, 45)
Length of Tuple: 5
Tuple Slice (1:4): (67, 3, 2)
Concatenated Tuple1 + Tuple2: (8, 67, 3, 2, 45, 60, 70, 80, 90, 100)
The even numbers in the tuple are: (8, 2)
The odd numbers in the tuple are: (67, 3, 45)
(base) aids@aids-OptiPlex-3000:~$'''