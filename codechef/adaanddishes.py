def minimum_cook_time(times):
  total_cook_time = 0
  if len(times)%2 == 0:
    for turn in range(int(len(times)/2)):
      total_cook_time += times[turn] + times[(turn*-1)-1]
  else:
    for turn in range(int((len(times)-1)/2)):
      total_cook_time += times[turn] + times[(turn*-1)-1]
    total_cook_time += times[int((len(times)-1)/2) + 1]
  return total_cook_time

def organise_times(times):
  for time in range(len(times)):
    times[time] = int(times[time])
  times.sort()

with open('adaanddishes.txt') as f:
  lines = [line.rstrip() for line in f]

times = []
# loop number of test cases
test_cases = int(lines[0])
for x in range(test_cases):
  # capture test case
  plates = int(lines[(x*2)+1])
  times = lines[(x*2)+2].split(" ")
  # sort and convert times
  organise_times(times)
  # calculate and print minimum cook time
  print(minimum_cook_time(times))  

# time counter
# sort time
# validate if it is odd or even
# add last and first 