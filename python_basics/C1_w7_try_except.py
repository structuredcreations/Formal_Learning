#7
#2
#bob
#10
#4


#print large, smallest
#if not number then ignore and send message

Largest = 0
smallest=9999999999999


while True:
    sval=input("Enter a number: ")
    if sval=="done" :
        break

#assign blank if non number is entered
    try:
        fval = int(sval)

        if fval > Largest :
            Largest=fval

        if smallest > fval :
            smallest=fval

    except:
        fval=None
        x = "Invalid input"
        #print("Input is not a number, try again")



print(x)
print("Maximum is",Largest)
print("Minimum is",smallest)
