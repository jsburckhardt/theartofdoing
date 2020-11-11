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
  base = [7]*n
  for i in product(*[range(1,i) for i in base]):
    b = []
    complex_algorith(n,i,b)
    if i[0] == 5:
      print(f"{i},{b},{expected_b}\n")
    if tuple(b) == expected_b:
      print(i)
    # for j in range(len(count)):
    #     print( '{0:3} , {1:3} , {2:1}'.format(first_index, table[i[j]][j], j+1))
    # first_index += 1


N = 5
a = [2,6,5,3,4]
expected_b = [5,2,3,4,5]
b = []
find_a(N,expected_b)
# complex_algorith(N,a,b)
# generate_sample_a(4)
# print(b)
# if b == processed_b:
#   print("party my friend")

