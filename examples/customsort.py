#!/usr/bin/python3 -tt

# example of doing custom sort using "key" fnction

# say we want to sort a list of names but with respect to last character.

def main():
  x = ['aaz', 'aat','ab', 'aav', 'abv', 'acc', 'ac', 'a']

  print('Default way sorted() works')
  print(x)
  # This sorts with respect to first char then the second char and so on.
  print(sorted(x))

  # as it turns out sorted() has an optional parameter named 'key'.
  # key take a function with 1 argument,
  # applies the function on each member of the list(well not really),
  # then sorts and then returns the sorted list,
  # as if the function was never applied to the elements

  # the following function just returns the last char in a string
  def last_char(s):
    return s[-1]

  print()

  print('now for the custom sorts')
  
  print(x)

  print(sorted(x, key = last_char))

  print()

  # now we want to sort the list first with respect to the last char,
  # the with respect to length of the string
  # so ['aab', 'ab', 'aa'] yields ['aa' , 'ab', 'aab']

  y = ['aab', 'ab', 'aa']

  # sorting a list of tuples is kind of like nested sorting which we're after.
  def last_char_len(s):
    return (s[-1], len(s))

  print(y)

  print(sorted(y, key = last_char_len))
  
  print()  

if __name__ == '__main__':
  main()
