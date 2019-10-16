"""
Fia Berggren Lindqvist
Windows 10
"""

print("Welcome, here you can check if a word or sentence is a palindrome") #Welcomes the user to the programme
palindrom = input("Please write a palindrome: ").lower() #This user writes their palindrome

reverse = ""

not_valid = ("§!¤%&/()=?`^*;:,.-_@£$€{[]}\'~ ")#A variable for which signs to not take into account

i=0

while i < len( not_valid ):
    palindrom = palindrom.replace(not_valid[i], "")
    i = i + 1 #While function is to remove invalid signs in the variable "not_valid" 

palindrom = palindrom.lower() #converts all letters to lowercase

#This code flips it and checks the palindrome
j = len(palindrom)-1
while j >= 0:
    reverse = reverse+(palindrom[j])
    j -= 1

if palindrom == reverse: #compare if the variable is the same from both directions/ that is equal to itself but backwards
    print("Yes, your input is a palindrome!") #if its the same, then it's a palindrome
else:
    print("No, your input is not a palindrome!") #if not then it's not a palindrome
