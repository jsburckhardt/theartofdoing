# import memory_profiler
from itertools import product

# @profile
def complex_algorith(n,a,b):
  for i in range(n):
    j = n-1
    while j >= 0:
      if a[j] % a[i] == 0:
        b.append(j+1)
        break
      else:
        j -= 1

def find_a(n,expected_b):
  # batches = [[1,10],[11,100],[101,1000],[1001,10000],[10001,100000],[100001,1000000],[1000001,4000000]]
  # for batch in batches:
  base = [n]*n
  for i in product(*[range(1,i) for i in base]):
    b = []
    complex_algorith(n,i,b)    
    if b == expected_b:
      return(i)



quantity_test_cases = int(input())
for x in range(quantity_test_cases):
  N = int(input())
  expected_b_input = input().split(" ")
  expected_b = [int(i) for i in expected_b_input]
  print(*find_a(N,expected_b))

# # N = 5
# N = 4
# # a = [2,6,5,3,4]
# expected_b = [5,2,3,4,5]
# expected_b = [4,4,4,4]
# b = []
# print(*find_a(N,expected_b))

