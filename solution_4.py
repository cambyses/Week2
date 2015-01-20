def syr(x):
    # for even
    if x%2 == 0: 
        return int(x/2)
       # for odd
    elif x%2 == 1: 
        return 3*x + 1

def main():
    x = int(input("Enter a starting Natural value: "))
    if x < 1:
        print ("Not a Natural Number")
    else:
        print ("The Syracruse sequence with the starting Natural value",x,"is: ")
        print (x)
        while x!= 1:
            x = syr(x)
            print (x)

main()
