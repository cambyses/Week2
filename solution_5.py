import math

def prime(n):
    sq = int(math.sqrt(n))
    i = 2
    while i<=sq:
        if n%i == 0:
            return False
        else:
            i=i+1
    return True

def main():
    n = int(input("Enter a number: "))
    if prime(n) == True:
        print ("The number",n,"is a prime")
    else:
        print ("The number",n,"is not a prime")

main()
