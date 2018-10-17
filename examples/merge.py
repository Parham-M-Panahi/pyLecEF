#!/usr/bin/python3 -tt

# Mergeing 2 lists.
# merging is a part of a sorting algorithm called merge sort,
# which you can do as part of the exercises.

# this is what the merge process looks like
# [1, 2, 4] , [3, 5] yields [1, 2 , 3, 4, 5]
# and 
# [1, 1, 4, 7], [2, 5] yields [1, 1, 2, 4, 5, 7]
# and so on. assume lists are sorted, original lists can be modified.

def merge(l1, l2):
  l = []
  while len(l1) > 0 and len(l2) > 0:
    if l1[0] <= l2[0]:
      l.append(l1.pop(0))
    else:
      l.append(l2.pop(0))

  l = l + l1 + l2
  return l

# this algorithm should be linear since we go though each element only once
# but as it turns out, time complexity of pop(0) is O(n), so the algorithm,
# becomes quadratic.
# pop() is constant though, and in the exercises you're encouraged
# to implement merge sort using a linear merge function.


def main():
  # let's test merge().
  l1 = [1, 2, 4]
  l2 = [3, 5]
  print(l1, l2)
  print(merge(l1, l2))

  print()

  x = [1, 1, 4, 7]
  y = [2, 5]
  print(x, y)
  print(merge(x, y))

if __name__ == '__main__':
  main()
