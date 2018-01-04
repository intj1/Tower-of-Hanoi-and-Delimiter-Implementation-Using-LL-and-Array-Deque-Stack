import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  check = Stack()
  dictionary = {"]":"[", "}":"{", ")":"("}
  for i in open(filename):
      for char in i:
          if char == "(" or char == "[" or char == "{":
              check.push(char)
          elif char == ")" or char == "]" or char == "}": 
              if dictionary[char] == check.peek():
                  check.pop()
              else:
                  return False
  if len(check) == 0:       
      return True

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


