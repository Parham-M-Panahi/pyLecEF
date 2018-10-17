#!/usr/bin/python3

# Compute the n'th fibonacci number.
# fib(n) = fib(n - 1) + fib(n - 2)
# fib(0) = 0, fib(1) = 1

# using the recursive definition of the fibonacci series
# this takes exponential time
def fib0(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib0(n - 1) + fib0(n - 2)



def fib1(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a
  


def main():
  for i in range(100):
    print(fib1(i))

  for i in range(100):
    print(fib0(i))




if __name__ == '__main__':
  main()
