#Function that takes a string and prints the letters in decreasing order of frequency.

def most_frequent(string):
  dictionary = dict()
  for key in string:
      if key not in dictionary:
          dictionary[key] = 1
      else:
          dictionary[key] += 1
  return dictionary

print(most_frequent('Mississippi'))

