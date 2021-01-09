#recursion variant
def main():
    num = int(input('enter number' ))
    print(fact_rec(num))
def fact_rec(n):
    if n==0 or n==1:
        return 1
    return n * fact_rec(n-1)

main()


# my previous variant
try:
    number = int(input('enter the number, which factorial should be calculated '))
    fact = 1
    for i in range(1,number + 1):
        fact *=i
        print(i, end='*')
    print(' = ', fact)
except ValueError:
    print ('the number is not integer')