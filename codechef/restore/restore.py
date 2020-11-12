# Calculate prime numbers
def sieve_of_eratosthenes(n): 
    primes = []
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1): 
        if prime[p]: 
            primes.append(p)
    return(primes)

# max number of primes
primes = sieve_of_eratosthenes(4000001)

# get quantity of test cases
quantity_test_cases = int(input())

for x in range(quantity_test_cases):
  # capture length of sample
  n = int(input())
  # capture b
  b_input = input().split(" ")
  b = [int(i) for i in b_input]
  # start calculating a
  a = []
  map = {}
  for i in b:
    map[i] = map.pop(i) + 1 if i in map else 1
  for i in range(n):
    a.append(primes[b[i]])
    map[b[i]] = map.pop(b[i])-1
  print(*a)
