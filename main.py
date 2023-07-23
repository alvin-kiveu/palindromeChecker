#CREATING A FUNCTION TO CHECK IF A STRING IS A PALINDROME OR NOT

def palindromeChecker(userInput):
    length = len(userInput)
    for i in range(length):
        if userInput[i] != userInput[length-i-1]:
            return False
    return True

#ASKING USER TO INPUT A STRING THAT HE/SHE WANTS TO CHECK IF IT IS A PALINDROME
input_string = input("Enter a string: ")
input_string = input_string.lower()

if palindromeChecker(input_string):
    print("The input string is a palindrome!")
else:
    print("The input string is not a palindrome.")
    
#END OF CODE

          
