mag = []
iron = []

quantity_test_cases = int(input())
while quantity_test_cases:
  quantity_test_cases -= 1
  i,j,m = 0,0,0
  n,k = [int(i) for i in input().split(' ')]
  s = input().upper()
  p = k +1
  l, r, count = 0,0,0

  for i in range(n):
    if s[i] == 'M':
      mag.append(i)
    if s[i] == 'I':
      iron.append(i)
    if s[i] =='X' or i == (n-1):
      while mag and iron:
        sheet = 0
        l = min(mag[0],iron[0])
        r = max(mag[0],iron[0])
        q = l
        while q <= r:
          if s[q] == ':':
            sheet += 1
          q +=1
        if p - abs(l-r) - sheet > 0:
          count += 1
          mag.pop()
          iron.pop()
        elif mag[0] < iron[0]:
          mag.pop()
        else:
          iron.pop()
      while mag:
        mag.pop()
      while iron:
        iron.pop()
  print(count,end='\n',flush=True)