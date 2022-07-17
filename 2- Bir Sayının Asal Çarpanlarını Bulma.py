def print_factors(aa):
    for i in range(1, aa + 1):
       if aa % i == 0:
           print(i)

num=int(input("Please give a number : "))

print_factors(num)