def isitpalindrome(vocable):

    if len(vocable)<=1:
        print("Palindrome")
        return
    else:
        if vocable[0]!=vocable[-1]:
            print("Not a palindrome")
            return
        return isitpalindrome(vocable[1:len(vocable)-1])

vocable=input("Enter vocable")

isitpalindrome(vocable)