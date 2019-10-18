# Implement a function/method that is given two strings and returns whether one can be obtained
# by the other after removing exactly one character. 
# Specifically, given two strings x and y, return true if and only if (1) x can be obtained by removing one
# character from y and/or (2) if y can be obtained by removing one character from x.

# Assume that both strings only contain English alphabets and that neither is an empty string.
# Note that x and y can be quite long (each containing millions of characters).

# Speed Complexity: O(n) where 'n' is the size of param 'x' || Space Complexity: O(1)
def equalsWhenOneCharRemoved(x, y):
  # Initial checks
  if abs(len(x) - len(y)) > 1 or len(x) == len(y):
    return False

  b_list = ""
  s_list = ""
  if len(x) > len(y):
    b_list = x
    s_list = y
  else:
    b_list = y
    s_list = x

  one_off = False
  s_index = 0

  for i in range(len(b_list)):
    if len(s_list) == s_index:
      return not one_off
    elif b_list[i] != s_list[s_index] and one_off == True:
      return False
    elif b_list[i] != s_list[s_index] and one_off == False:
      one_off = True
      continue
    s_index += 1

  return one_off
