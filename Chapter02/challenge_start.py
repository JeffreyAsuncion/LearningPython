# create a checkPalindrome function
# Enter string to test for palindrome

def checkPalindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

def main():
    word = 'palidrome'
    while(word != 'exit'):
        word = input("Enter string to test for palindrome or 'exit' : ")
        if checkPalindrome(word):
            print("Yes, it is!")
        else:
            print("Nope, not a palidrome")

if __name__ == '__main__':
    main()