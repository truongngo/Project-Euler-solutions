i = 6
n = 14

def isPrime(x):
    if x == 2:
        return True
    else:
        for i in range(2,x):
            if x%i == 0:
                return False; break
        return True
            
while i < 10001:
    if isPrime(n):
        i = i+1
        if i == 10001:
            print n
            break
    n = n+1