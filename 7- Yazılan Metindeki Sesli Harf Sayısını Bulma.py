def vowels_list(x):
    vowels = 0
    for i in str(x):
         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
             vowels = vowels + 1
    print("Sum of Vowels: ", vowels)



vowels_list(input("Enter string: "))