def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        count = 3
        prev = 1
        fib = 1
        while count <= n:
            tmp = fib
            fib = fib + prev
            prev = tmp
            count = count + 1
        return fib
    else:
        return 0

def main():
    num = int(input("Enter the number n: "))
    result = Fibonacci(num)
    print("The Fibonacci number is: ",result)

main()
