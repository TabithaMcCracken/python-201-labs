# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(num_list):
  # define the function here
  """Find max,  min and average of numbers

  Args:
      num_list ([int]): [numbers used]
  """
  max_num = max(num_list)
  min_num = min(num_list)

  total = 0
  for num in num_list:
    total += num
  num_average = total/len(num_list)

  totals = [max_num, min_num, num_average]

  return totals
# call the function below here
list_outputs = stats(example_list)
print("Here is the highest number: ")
print(list_outputs[0])

print("Here is the lowest number: ")
print(list_outputs[1])

print("Here is the average of the list: ")
print(list_outputs[2])