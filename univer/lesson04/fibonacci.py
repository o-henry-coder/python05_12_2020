#recursion variant
def main():
    num = int(input('choose fibonacci number to show ' ))
    print(fibonacci_number(num - 1))
def fibonacci_number(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

main()