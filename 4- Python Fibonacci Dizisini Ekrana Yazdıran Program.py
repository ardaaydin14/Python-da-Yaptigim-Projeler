def  fibonacci(boundary):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range(boundary-2):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
boundary=int(input("Give a number = "))
fibonacci(boundary)