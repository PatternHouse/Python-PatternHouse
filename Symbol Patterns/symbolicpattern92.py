def generate_pattern():
  rows = 8  # Total number of rows (odd number to form the shape)

  for i in range(rows):
    if i == 0 or i == rows - 1:
      print(" " * 6 + "*")
    elif i == 1 or i == rows - 2:
      print(" " * 5 + "- -")
    elif i == 2 or i == rows - 3:
      print(" " * 4 + "-   -")
    elif i == 3 or i == rows - 4:
      print(" " * 3 + "-     -")


generate_pattern()