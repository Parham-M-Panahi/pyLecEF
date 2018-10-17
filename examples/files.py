#!/usr/bin/python3 -tt

# how to open and read from text files.

def main():

  # first you need a file handle.
  file_handle = open('sample.txt', 'r')

  # you iterate over a file line by line.
  for line in file_handle:
    print(line, end = '')

  file_handle.close()

  print('\n')

  # you can read files into a string.

  file_handle = open('sample.txt', 'r')

  text = file_handle.read()

  lines = text.split('\n')
  print(lines)

  file_handle.close()

  print('\n')

  # or you can read files directly into a list of lines.
  file_handle = open('sample.txt', 'r')

  lines = file_handle.readlines()

  print(lines)
    

if __name__ == '__main__':
  main()
