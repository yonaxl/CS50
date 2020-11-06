def main():
    num = input("Please input the credit card number to validate : ")
    num1 = []
    for n in num:
        if int(n) >= 0 :
            num1.append(n)
    if checksum(num1) == True:
        if checkvalid(num1) == True:
            if num[0] == "4":
                print("VISA\n")
            elif num[0] == "5" or num[0] == "2":
                print("MASTERCARD\n")
            elif num[0] == "3":
                print("AMEX\n")
            elif num[0] == '6':
                print("DISCOVER\n")
            else :
                print("VALID")
        else:
            print("INVALID")
    else:
        print("INVALID")
    
def checksum(x):                    #checking the total input number amounts to 16
    if len(x) == 16:
        return True
    else :
        return False

def checkvalid(x):                  #check the validity using Luhn's algorithm
    check1 = ""
    check11 = ""
    ttl = 0
    check2 = ""
    for n in range(16):             #collecting the every other number
        if n %2 == 0:
            check1 += x[n]
        else:
            check2 += x[n]
    for n in check1:                 #multiply by 2
        check11 += str(int(n)*2)
    for n in check11:                #add them all together
        ttl += int(n)
    for n in check2:
        ttl += int(n)
    if ttl % 10 == 0:
        return True
    
main()