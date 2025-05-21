# String Operations
# Name: Ganesh Wagh
# Branch: FY-B.Tech AIDS-B3
# Roll No: 133

word = input("Enter your string: ")

# Check if the string is palindrome
if word == word[::-1]:
    print("Your string is a palindrome.")
else:
    print("Your string is not a palindrome.")

# Convert to upper and lower case
up_word = word.upper()
lw_word = word.lower()
print(f"Uppercased word: {up_word}")
print(f"Lowercased word: {lw_word}")

# Find a letter in the string
f = input("Enter an element you want to find in the string: ")
index = word.find(f)
if index != -1:
    print(f"Your element '{f}' is present in the string at index: {index}")
else:
    print(f"Your element '{f}' is not found in the string.")

'''******OutPut******
(base) (base) aids@aids-OptiPlex-3000:~/Mayur FY - Aids B$ python3 mayur5.py
Enter your string: Mayur
Your string is not a palindrome.
Uppercased word: MAYUR
Lowercased word: mayur
Enter an element you want to find in the string: u
'''