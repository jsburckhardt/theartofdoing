def organise_times(times):
  for time in range(len(times)):
    times[time] = int(times[time])
  times.sort()

def cook_status(cooking_burner, times, cooking_time):
  # Empty cooktop and plates in queue
  if not cooking_burner and len(times) > 0:
    cooking_state = True
    cooking_time = times.pop()
    return cooking_state, cooking_time
  # cooking time is done
  elif cooking_time <= 0:
    return False, 0
  # still cooking
  else:
    return cooking_burner, cooking_time

def cook(plates, times):
  # define variables
  cooking_burner_1 = False
  cooking_burner_2 = False
  cooking_time_1 = 0
  cooking_time_2 = 0
  cooking = True if len(times) > 0 else False
  total_cook_time = 0

  # while cooking
  while cooking:
    cooking_burner_1, cooking_time_1 = cook_status(cooking_burner_1,times, cooking_time_1)
    cooking_burner_2, cooking_time_2 = cook_status(cooking_burner_2,times, cooking_time_2)
    
    total_cook_time += 1
    cooking_time_1 -= 1
    cooking_time_2 -= 1

    # verify if cook done
    cooking_burner_1, cooking_time_1 = cook_status(cooking_burner_1,times, cooking_time_1)
    cooking_burner_2, cooking_time_2 = cook_status(cooking_burner_2,times, cooking_time_2)
  
    if not cooking_burner_1 and not cooking_burner_2 and len(times) == 0:
      cooking = False
  print(total_cook_time)

# Load file
with open('adaanddishes.txt') as f:
  lines = [line.rstrip() for line in f]

# Loop test cases and load times and length
times = []
total_cook_times = []
quantity_test_cases = int(lines[0])
for x in range(quantity_test_cases):
  # capture test case
  plates = int(lines[(x*2)+1])
  times = lines[(x*2)+2].split(" ")
  # sort and convert times
  organise_times(times)
  
  # start cooking
  cook(plates, times)

