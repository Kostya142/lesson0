numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
for i in numbers:
    z=True and i!=1
    for k in range(2, i):
        if i % k == 0:
          not_primes.append(i)
          z=False
          break
    if  z==True:
        primes.append(i)
print(not_primes)
print(primes)