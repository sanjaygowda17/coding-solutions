# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a, b = input().split()
    try:
        z = int(a)//int(b)
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:', e)
    else:
        print(z)  
