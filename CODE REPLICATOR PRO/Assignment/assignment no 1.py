'''Title: - write a python code to create a list and perform the
following operations on it.
Name = Ganesh Wagh
roll no = 133
Branch = Aids- B3'''
a = int(input("Enter the number of elements in the list 1: "))
b = int(input("Enter the number of elements in the list 2: "))
c = int(input("Enter the number of elements in the list 3: "))
d = int(input("Enter the number of elements in the list 4: "))
e = int(input("Enter the number of elements in the list 5: "))
list = [a, b, c, d, e]
print("The list is: ", list)
print("The length of the list is: ", len(list))
print("The sum of the list is: ", sum(list))
print("The maximum element in the list is: ", max(list))
print("The minimum element in the list is: ", min(list))
list.append(6)
print("The append operation on the list is: ", list)
list.remove(6)
print("The delete operation on the list is: ", list)
list.pop(2)
print("The pop operation on the list is: ", list)
list.reverse()
print("The reverse operation on the list is: ", list)
#*Output*********
'''
(base) aids@aids-OptiPlex-3000:~$ python3 Ganesh Wagh.py
Enter the number of elements in the list 1: 44
Enter the number of elements in the list 2: 55
Enter the number of elements in the list 3: 66 
Enter the number of elements in the list 4: 89
Enter the number of elements in the list 5: 99
The list is: [44, 55, 66, 89, 99]
The length of the list is: 5 
The sum of the list is: 353
The maximum element in the list is: 99
The minimum element in the list is: 44
The append operation on the list is: [44, 55, 66, 89, 99, 6]
The delete operation on the list is: [44, 55, 66, 89, 99]
The pop operation on the list is: [44, 55, 89, 99]
The reverse operation on the list is: [99, 89, 55, 44]
(base) aids@aids-OptiPlex-3000:~$
'''