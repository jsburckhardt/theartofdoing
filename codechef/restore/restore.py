import memory_profiler

@profile
def complex_algorith(n,a,b):
  for i in range(n):
    j = n-1
    while j >= 0:
      if a[j] % a[i] == 0:
        b.append(j+1)
        break
      else:
        j -= 1
    
    # j_opts = []
    # for j in range(n):
    #   if a[j] % a[i] == 0:
    #     j_opts.append(j+1)
    # b.append(max(j_opts))


if __name__ == '__main__':
  N = 5
  a = [2,6,5,3,4]
  # b = [5,2,3,4,5]
  b = []

  complex_algorith(N,a,b)
  print(b)
# if b == processed_b:
#   print("party my friend")

