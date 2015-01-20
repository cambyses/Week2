def main():
    dist_total = 0.0
    gas_total = 0.0
    filename = input("Enter the name of the file: ")
    infile = open(filename, 'r')
    line = infile.readline()
    start_first = float(eval(line))
    start_leg = start_first
    line = infile.readline()
    count = 1
    while line != "":
        end_leg = -1.0
        for num in line.split(" "):
            if end_leg == -1.0:
                end_leg = float(eval(num))
            else:
                gas_leg = float(eval(num))
        print ("MPG for leg number",count,"is: ", float((end_leg-start_leg)/gas_leg))
        start_leg = end_leg
        gas_total = gas_total+gas_leg
        line = infile.readline()
        count = count + 1
    mpg_final = float((end_leg-start_first)/gas_total)
    print ("Total MPG is: ", mpg_final)
    
main()
