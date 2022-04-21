from collections import Counter

def solution(string: str) -> int:
  """
  Find the longest substring that contains an equally many of each character.
  
  The approach is to use a sliding window, which starts with the full string
  and halts on a window of size 1 (aka, a single character). This will work
  for all strings from size N to size 1. We finish early on windows of size 1
  as we match against the first character, which is sufficient. Empty strings
  are skipped over by the window (range(x, x) == []) so we return 0 after it.
  
  I am not handling the broken test cases from Google. This is just a minimum
  solution that I feel is clear and concise.
  """
  
  for w in range(len(string), 0, -1): # window size
    for i in range(len(string) - w + 1): # window's first index
      window = string[i:i + w]
      counts = Counter(window) # occurences of each letter
      target = counts[window[0]] # how many occurences we need
      if all(c == target for c in counts.values()):
        return w # the window is the size of the longest substring
  
  return 0 # empty string
