##Paint_Rangoli Function
def print_rangoli(n):
    
    for i in range(n):
        alpha = chr(96 + n)
        count = 0
        for j in range(n):
            if (j >= (n - 1 - i)):
                if (j == (n-1)):
                    print(alpha, end = "")
                else:
                    print(alpha, end = "-")
                    alpha = chr(ord(alpha) - 1)
                count += 1
            else:
                print("-", end = "-")
                
        for k in range(n-1):
            if (count > 1):
                alpha = chr(ord(alpha) + 1)
                print("-", end = alpha)
                count -= 1
            else:
                print("-", end = "-")
        
        print()
        
    for i in range(1,n):
        alpha = chr(96 + n)
        count = 0
        for j in range(n):
            if (j >= i):
                if (j == (n - 1)):
                    print(alpha, end = "")
                else: 
                    print(alpha, end = "-")
                    alpha = chr(ord(alpha) - 1)
                count += 1
            else:
                print("-", end = "-")
    
        for k in range(1,n):
            if (count > 1):
                alpha = chr(ord(alpha) + 1)
                print("-", end = alpha)
                count -= 1
            else:
                print("-", end = "-")
        
        print()
        
##Main Function
n = int(input())
print_rangoli(n)