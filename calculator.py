#Calculator
print("********************CALCULATOR********************")
print()
print()
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
print()
print()
print("[1] ADDITION")
print("[2] SUBTRACTION")
print("[3] MULTIPLICATION")
print("[4] DIVISION")
print()
print("-----------------------------")
print()
c = int(input("Select any one of the above operation : "))
print()
if(c==1):
        d = a+b
        print()
        print("^^^^^^^^PERFORMING ADDITION^^^^^^^^")
        print()
        print("RESULT IS :",d)
elif(c==2):
    e = a-b
    print()
    print("^^^^^^^^PERFORMING SUBTRACTION^^^^^^^^")
    print()
    print("RESULT IS :",e)
elif(c==3):
    f = a*b
    print()
    print("^^^^^^^^PERFORMING MULTIPLICATION^^^^^^^^")
    print()
    print("RESULT IS :",f)
elif(c==4):
    g = a/b
    print()
    print("^^^^^^^^PERFORMING DIVISION^^^^^^^^")
    print()
    print("RESULT IS :",g)
else:
    print()
    print("-----WRONG CHOICE-----")
    
