n = 1

while n < 8:
    print("Please input a height of 8 or more... type numbers only please...")
    n = int(input("Height : "))

for i in range(n):
    nn = i + 1
    print((" "*(n-nn)) + ("#"*nn) + "  " +  ("#"*nn) + (" "*(n-nn)) )
