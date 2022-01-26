print("Pattern Printing")
num = int(input("How many rows you want to print? "))
bool_val = input("Enter 1 for True value or 0 for False value : ")
if bool_val == "1":
    for i in range(0, num+1):
        print("*"*int(i))
if bool_val == "0":
    for i in range(num, 0, -1):
        print("*"*int(i))
