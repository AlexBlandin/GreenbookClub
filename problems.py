from math import log10, log2, ceil, floor, sqrt
from random import randint, sample
from itertools import combinations

BLOCKY_ASTR = True

def astr(arr, sep=" "): # Because join only takes arrays of strings
  return sep.join([str(a) for a in arr])

def bastr(arr, sep=" "): # Because join only takes arrays of strings
  if BLOCKY_ASTR: return "".join(["█" if a == 1 else " " for a in arr])
  else: return astr(arr, sep)

def p1(explain=True, n=20):
  """
  Problem 1.1
    Given a list of n numbers, return/print out a new list
    containing all the even elements of the original list,
    followed by all the odd elements of the original list.
    So long as it is <evens> followed by <odds>, they can be in any order.

     51 42 43 67 46
     > 42 46 51 43 67

  Problem 1.2
    Extend Problem 1.1, by formatting your outputs, namely
    the output evens are in ascending order (2, 4, 6),
    and the output odds are in descending order (5, 3, 1).

     51 42 43 67 46
     > 42 46 67 51 43
  """
  
  biggest_number = 99 # random, so might not see
  numbers = [randint(0, biggest_number) for _ in range(n)]

  print()
  print("Problem 1.1")
  if explain:
    print(f"For example, a list of {n} elements might be: ")
  print()
  print(f" {astr(numbers)}")
  print()
  input("Press enter/return to see the result: ")
  
  print()
  odds = {}
  for num in numbers:
    if num % 2:
      odds[num] = odds.get(num, 0) + 1 # not using setdefault, :shrug:
    else:
      print(num, end="")

  for num in odds:
    for _ in range(odds[num]):
      print(num, end="")
  print()
  print()
  input("Press enter/return to see Problem 1.2 ")

  print()
  print("Problem 1.2")
  if explain:
    print(f"For example, a list of {n} elements might be: ")
  print()
  print(f" {astr(numbers)}")
  print()
  input("Press enter/return to see the result: ")
  
  # Timsort is O(n log n) at worst (merge), O(n) at best (insertion/reverse)
  # So we have best case O(n), average O(n log n/2), and worst case O(n log n)
  # Where roughly exact is O(n log nr) where r is the ratio odds & evens >= 0.5
  # We can intuitively see the speedup, as we don't "merge" back together for
  # that final step, which is the benefit of having two disjoint halves on average.
  # Otherwise, we are bound to the larger of the two, so the "significant portion"
  # of the ratio between odds and evens (the 7 of 7:3 as 0.7) gives O(n log nr).
  odds, evens = {}, {}
  for num in numbers:
    if num % 2:
      odds[num] = odds.get(num, 0) + 1
    else:
      evens[num] = evens.get(num, 0) + 1

  print()
  for num in sorted(evens):
    for _ in range(evens[num]):
      print(num, end=" ")

  for num in sorted(odds, reverse=True):
    for _ in range(odds[num]):
      print(num, end=" ")
  print()


def p2(explain=True, n=10):
  """
  Problem 2
    Given a matrix of size n*n, where the elements are either 1 or 0,
    find the largest "rectangle" where every element is 1.
  """
  
  matrix = [[randint(0, 1) for _ in range(n)] for _ in range(n)]
  counter = 0

  print()
  print("Problem 2")
  if explain:
    print(f"For example, a matrix of size {n}*{n} might be: ")
  print()

  largest, largest_size = None, None

  def size(rect):
    l, t = rect["left"], rect["top"]
    r, b = rect["right"], rect["bottom"]
    return (abs(l-r)+1)*(abs(t-b)+1)

  def coords(rect):
    return (rect["left"], rect["top"]), (rect["right"], rect["bottom"])

  def valid(rect):
    (left, top), (right, bottom) = coords(rect)
    return all([all([cell == 1 for cell in row[left:right+1]]) for row in matrix[top:bottom+1]])

  def no_point(i, j):
    return largest_size != None and abs((n-i)*(n-j)) <= largest_size

  print("  #" + "".join([str(i) for i in range(n)]))
  above, rects, graveyard = [set() for _ in range(n)], {}, set()
  for j, row in enumerate(matrix):
    print("  " + str(j).zfill(ceil(log10(max(n, 1)))), end="")
    print(bastr(row), end=" ")
    if no_point(0, j):
      print()
      continue # finish early, we have the largest

    # 0th pass, clear out
    for s in above:
      for rect_id in set(s): # clear backwards
        if rect_id in graveyard:
          s.discard(rect_id)
    for rect_id in graveyard: del rects[rect_id]
    graveyard.clear()

    # 1st pass, invalidate and trim
    for i, cell in enumerate(row):
      if cell == 0: # invalidate column, trim rects
        for rect_id in set(above[i]):
          if rect_id not in graveyard: # only die once
            rects[rect_id]["bottom"] = j - 1 # it ended before this row
            rect_size = size(rects[rect_id])
            if valid(rects[rect_id]) and (largest == None or rect_size > largest_size): # is it a candidate?
              largest, largest_size = dict(rects[rect_id]), rect_size # save a copy
            left = rects[rect_id]["left"]
            if i > left: # if we can save it by walking backwards, let's try
              counter += 1
              new_id = counter # we make a new one so that we can get rid of the old
              rects[new_id] = dict(rects[rect_id])
              rects[new_id]["right"] = i - 1
              for c in range(left, i - 1):
                above[c].add(new_id)
            graveyard.add(rect_id) # we're killing it, so don't forget

    # 2nd pass, generate and preserve
    rect, left = None, None
    for i, cell in enumerate(row):
      if cell == 1:
        if left == None:
          left = i
          fs = set(above[i])
          for rect_id in fs:
            counter += 1
            new_id = counter # make a new one that "inherits" the above rect
            rects[new_id] = dict(rects[rect_id])
            rects[new_id]["left"] = i
            for c in range(left, rects[new_id]["right"]+1):
              above[c].add(new_id)
            graveyard.add(rect_id)
        if largest != None and no_point(left, j): break # stop early
        if len(above[i] - graveyard) == 0 and rect == None: rect = {"left": left, "top": j} # new rect
      if cell == 0: # we know the bounds of this rect
        if rect == None or left == None:
          rect, left = None, None
        elif left != None:
          rect["right"] = i - 1 # the sequence of ones from the left
          counter += 1
          rect_id = counter
          rects[rect_id] = dict(rect)
          for c in range(left, i):
            above[c].add(rect_id)
          rect, left = None, None

    # Ended 2nd pass with a rect
    if rect != None and row[-1] != 0:
      rect["right"] = n - 1 # ended at edge
      counter += 1
      rect_id = counter
      rects[rect_id] = rect
      for c in range(left, n - 1):
        above[c].add(rect_id)
      rect, left = None, None
    print()

  # # Ended with rects
  # for i in range(n):
  #   fs = set(above[i])
  #   break
  #   for rect_id in fs:
  #     if rect_id not in graveyard:
  #       graveyard.add(rect_id)
  #       rects[rect_id]["bottom"] = n - 1
  #       rect_size = size(rects[rect_id])
  #       if valid(rects[rect_id]) and (largest == None or rect_size > largest_size):
  #         largest, largest_size = dict(rects[rect_id]), rect_size
  print()
  input("Press enter/return to see the result: ")
  print()
  if largest != None:
    start, finish = coords(largest)
    print(f"The largest rectangle is from {start} to {finish}, with size {largest_size}")
    print()
    print("  #" + "".join([str(i) for i in range(start[0],finish[0]+1)]))
    for i, row in enumerate(matrix[start[1]:finish[1]+1], start=start[1]): # just to make sure we're not crazy
      print("  " + str(i).zfill(ceil(log10(max(finish[1], 1)))), end="")
      print(bastr(row[start[0]:finish[0]+1])) # visually inspect
  else:
    print(" There was nothing in the matrix")

def p3(explain=True, n=10):
  """
  Problem 3
    Given a list of n integers, find all pairs that sum to zero.

     -9 3 9 0 -3
     > (9, -9) (3, -3)
  """
  
  biggest_number = 9
  numbers = [randint(-biggest_number, biggest_number) for _ in range(n)]
  numbers = numbers + [-x for x in numbers] + [0]*int(n/2)
  numbers = sample(sample(numbers, 2*n), n)

  print()
  print("Problem 3")
  if explain:
    print(f"For example, a list of {n} elements might be: ")
  print()
  print(f" {astr(numbers)}")
  print()
  input("Press enter/return to see the result: ")
  print()

  includes = {} # each number and its negative
  zeroes = 0 # how many zeroes there are in the list
  for x in numbers:
    if x > 0:
      if x not in includes: includes[x] = {"+": 0, "-": 0}
      includes[x]["+"] += 1

    if x < 0:
      x = -int(x) # just to shut up the linter
      if x not in includes: includes[x] = {"+": 0, "-": 0}
      includes[x]["-"] += 1

    if x == 0:
      zeroes += 1

  if zeroes > 0 or len(includes) > 0:
    if zeroes > 1:
      print(" ".join(["(0, 0)"]*min(int(zeroes/2), 1)), end = " ")

    for x, d in includes.items():
      m = min(d["+"], d["-"])
      if m > 0:
        print(" ".join([f"({x}, {-x})"]*m), end=" ")
  else:
    print("No pairs in the list", end="")
  print()

def p4(explain=True, n=10):
  """
  Problem 4
    Extend Problem 3 such that you find all sets of 3 integers that sum to zero.

     0 9 0 0 2
     > (0, 0, 0)

     -5 -4 4 7 0
     > (-4, 0, 4)

     -9 0 -3 -3 3 -5 0 0 5 2
     > (-5, 0, 5) (-5, 2, 3) (-3, 0, 3) (0, 0, 0)
  """
  
  biggest_number = 9
  numbers = [randint(-biggest_number, biggest_number) for _ in range(n)]
  numbers = numbers + [-x for x in numbers] + [0]*n # get useful examples
  numbers = sample(sample(numbers, 2*n), n) # oversample, then get n, for more repeats

  print()
  print("Problem 4")
  if explain:
    print(f"For example, a list of {n} elements might be: ")
  print()
  print(f" {astr(numbers)}")
  print()
  input("Press enter/return to see the result: ")
  print()

  if numbers.count(0) > 3: print("(0, 0, 0)", end = " ") # set(numbers) eliminates extra 0s so test here
  for a, b, c in [tuple(combo) for combo in combinations(sorted(list(set(numbers))), 3)]:
    if a + b + c == 0:
      print(f"({a}, {b}, {c})", end = " ")
  print()

  # ([print("(0, 0, 0)", end = " ") if numbers.count(0) > 3 else None]+[print(c, end = " ") for c in combinations(sorted(list(set(numbers))), 3) if sum(c) == 0]+[print()]) * 0
  # " ".join((["(0, 0, 0)"] if numbers.count(0) > 3 else []) + [str(c) for c in filter(lambda c: sum(c)==0, combinations(sorted(list(set(numbers))), 3))])

def p5(explain=True, n=7):
  """
  Problem 5
    Given an input containing parenthesis, write a function to decide
    if the parenthesis are matched. That is, for every opening parenthesis
    there must be a unique corresponding closing parenthesis and vice versa.

     (()())()
     ? Yes

     ()(())(())(())()
     ? True

     (print)((Google())Green)(((Book)))
     ? Yes

     d)(f(*o')F))r
     ? No

     print(Book)()(())
     ? Yes

     (Hello)(()(m)ain)))
     ? No

     (Hello)(((int))(H)ello)(print)(())((()))
     ? Yes
  """
  
  s = ""
  lexicon = ["Hello", "world", "main", "int", "print", "lithp", "Google", "Green", "Book"]

  # Lithp - definition of Lithp by The Free Dictionary (https://www.thefreedictionary.com/Lithp)
  # Lithp. n. One of the first high-level programming languages, designed to handle complex data structures.

  o = 0
  c = 0
  i = 0
  while o < n and c < n: # generate valid s with stuff from lexicon
    i += 1
    x = randint(0, 2)
    if i > n:
      x = randint(1, 2)
    if o + x <= n:
      s += "(" * x
      o += x
    x = randint(0, 1)
    if o + x <= n:
      s += "(" * x
      o += x
    for l in sample(lexicon, randint(0, 1)):
      s += l
    if i > n:
      x = randint(1, 2)
    x = randint(0, 2)
    if c + x <= n and c + x <= o:
      s += ")" * x
      c += x
    x = randint(0, 1)
    if c + x <= n and c + x <= o:
      s += ")" * x
      c += x
  if c < o: s += ")" * (o-c)

  if randint(0, 2) == 1 and len(s) > 1: # corrupt that string
    if randint(0, 3) == 1: # generate a real garbled string
      s = "".join(sample("".join([chr(ord(c) + randint(-1, 1)) for c in s]), len(s)))
    else: # drop some random parens and/or add new ones in
      what_to_do = randint(0, 4)
      s = list(s)
      if what_to_do in [0, 1]: # drop
        for _ in range(1, min(3, len(s))): # how many to drop
          del s[randint(0, len(s)-1)]
      if what_to_do in [1, 2, 4]: # add
        for _ in range(1, min(3, len(s))): # how many to add
          s.insert(randint(0, len(s)-1), "(" if randint(0,1) == 1 else ")")
      s = "".join(s)

  stack, matching = 0, True
  for c in s:
    if c == "(":
      stack += 1
    elif c == ")" and stack > 0:
      stack -= 1
    elif c != "(" and c != ")":
      continue
    else:
      matching = False
      break

  print()
  print(f" {s}")
  print(f" {'Yes' if stack == 0 and matching else 'No'}")

def p6(explain=True, n=100):
  """
  Problem 6
    Given 100 open doors, how many doors are left open if you were to close every other door, then open/close (toggle) every third door, then every fourth door, and so on until you open/close the final door?
  """
  
  print()
  print("Problem 6")
  print()
  print(f" 100 doors")
  print()
  input("Press enter/return to see the result: ")
  print()

  print(f" {floor(sqrt(100))} left open")

def p7(explain=True, n=100):
  """
  Problem 7
    Given any n doors, how many would be left open? Can you express this as an equation of d(n) = ???
  """
  
  print()
  print("Problem 7")
  print()
  print(f" {n} doors")
  print()
  input("Press enter/return to see the result: ")
  print()

  print(f" {floor(sqrt(n))} left open")

def p8(explain=True, n=10):
  """
  Problem 8
    Given a full stack and an empty stack, how can you sort the first stack (smallest items on top) using only standard operations and the second stack? How fast can you go?
  """
  
  biggest_number = 9
  numbers = [randint(0, biggest_number) for _ in range(n)]
  numbers = sample(numbers, n)

  print()
  print("Problem 8")
  if explain:
    print(f"For example, a list of {n} elements might be: ")
  print()
  print(f" {numbers}")
  print(" []")
  print()
  input("Press enter/return to see the result: ")
  print()

  print(f" {sorted(numbers, reverse=True)}")
  print(" []")

def p9(explain=True, n=10):
  """
  Problem 9
    Sort your full stack, but this time you can have as many additional stacks as you want. Can you go faster?
  """
  
  biggest_number = 9
  numbers = [randint(0, biggest_number) for _ in range(n)]
  numbers = sample(numbers, n)

  print()
  print("Problem 9")
  if explain:
    print(f"For example, a list of {n} elements might be: ")
  print()
  print(f" {numbers}")
  print(" []")
  print(" []")
  print(" []")
  print(" []")
  print()
  input("Press enter/return to see the result: ")
  print()

  print(f" {sorted(numbers, reverse=True)}")
  print(" []")
  print(" []")
  print(" []")
  print(" []")

def p10(explain=True, n=5):
  """
  Problem 10
    Given a positive integer, print the next smallest and next largest numbers that have the same number of 1 bits in their binary representation. Assume it is even.
  """
  
  number = [1]*n + [0]*int(n*0.5) # optional fudge factor for num 0s != 1s
  number = "".join([str(c) for c in (sample(number, len(number)) + [0])])
  number = int(number, 2) # base-2
  print()
  print("Problem 10")
  if explain:
    print(f"For example, a number with {n} true/1 bits might be: ")
  print()
  print(f" {number} ({number:b})")
  print()
  input("Press enter/return to see the result: ")
  print()

  lower = lambda x: ((x&-x)^x)|((x&-x)>>1)
  higher = lambda x: ((x | (x-1))+1) | x ^ (x & -x)

  print(f"  {lower(number)} < {number} < {higher(number)}")
  print(f"  {lower(number):b} < {number:b} < {higher(number):b}")

def p11(explain=True, n=5):
  """
  Problem 11
    What if you only assume it is a positive integer?
  """
  
  number = [1]*n + [0]*int(n*0.5) # optional fudge factor for num 0s != 1s
  number = "".join([str(c) for c in (sample(number, len(number)))])
  number = int(number, 2) # base-2

  print()
  print("Problem 11")
  if explain:
    print(f"For example, a number with {n} true/1 bits might be: ")
  print()
  print(f" {number} ({number:b})")
  print()
  input("Press enter/return to see the result: ")
  print()

  # lower_even = lambda x: ((x&-x)^x)|((x&-x)>>1)
  higher = lambda x: ((x | (x-1))+1) | x ^ (x & -x)

  lower = lambda x: ((x&-x)^x)|((x&-x)>>1) if not (x & 1) else ((x ^ ((((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))) & -(((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))))) | (((((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))) & -(((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1)))) >> 1))

  print(f" {lower(number)} < {number} < {higher(number)}")
  print(f" {lower(number):b} < {number:b} < {higher(number):b}")

# from num2words import num2words
def p12(explain=True, n=None):
  """
  Problem 12
    Given any number in the range ± 2 Billion, represent it as a string of natural written/spoken English.

      1234
      > one thousand, two hundred, and thirty-four

      -92435
      > minus ninety-two thousand, four hundred, and thirty-five
  """

  if n == None:
    n = randint(-2 * 10**9, 2 * 10**9)

  print()
  print("Problem 12")
  if explain:
    print(f"For example, given: ")
  print()
  print(f" {n}")
  print()
  input("Press enter/return to see the result: ")
  print()

  # print(num2words(n, lang="en_GB").replace(" and ", ", and "))

def p13(explain=True, n=None):
  """
  Problem 13
    You have a calculator that only has working addition and negation buttons (not subtraction, as in 4 to -4, and -4 to 4).

      A: Define subtraction using any or all of those two operations.

      B: Define multiplication using any or all of those two operations and subtraction.

      C: Define division using any or all of of those two operations, as well as multiplication and subtraction.

      (Hint, you may not need every available operations for each part.)
  """
  return

def p14(explain=True, n=10):
  """
  Problem 14.1
    An array a[] might have "magix indices", which is when a[i] == i. If it is unsorted, what is the most efficient algorithm?

  Problem 14.2
    And if a[] was sorted?
  """
  return

def p15(explain=True, n=5):
  """
  Problem 15
    Given a matrix of sizes NxM, create a new matrix of the same size where all rows and columns containing a 0 in the original matrix are themselves now all 0s.

    What's the complexity in both time and space of your algorithm? Can you go faster, or use less space?
    Can you do it without copying the matrix? (Don't try to be cheeky either.)

      1,2,3,4
      1,0,8,7
      4,4,0,2
      6,7,8,9
      1,2,3,4

    > 1,0,0,4
      0,0,0,0
      0,0,0,0
      6,0,0,9
      1,0,0,4
  """
  return

def p16(explain=True, n=5):
  """
  Problem 16
    Given an NxM matrix, describe an algorithm to search for a given value. The following properties hold for the matrix:

      1. Each row is comprised of integers sorted in ascending order (left to right)
      2. The first value on a given row is strictly greater than the last value of the row before it.

      For example, given

        1,   3,  5,  7
        10, 11, 16, 20
        23, 30, 34, 50

        ? 3
        > true

      How fast can you go? Why?
  """
  return

def p17(explain=True, n=5):
  """
  Problem 17.1
    Given the positive integer n, determine how many 2s appear in the numbers between 0 and n.

      25
      > 9
      ? 2, 12, 20, 21, 22, 23, 24, 25

    Assuming n < 10000, how fast can you go?

  Problem 17.2
    n is simply a positive integer. How fast can you go?
  """
  return

def p18(explain=True, n=5):
  """
  Problem 18.1
    Given a list of daily temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.

    If there are no future days for which this is possible, that day is assigned the value 0.

      73, 74, 75, 71, 69, 72, 76, 73
     > 1,  1,  4,  2,  1,  1,  0,  0

  Problem 18.2
    Can you do this in linear time?
    How much space does this require? Can you reduce that asymptotically?
  """
  return

def p19(explain=True, n=5):
  """
  Problem 19
    Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.

    Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

    Return the maximum number of rows that have all values equal (all 1s or all 0s) for any number of flips.

      0, 1
      1, 1
      > 1
      ? No flips required, the bottom row is the only one with equal values.

      0, 1
      1, 0
      > 2
      ? Flip the first column, both rows now count.

      0, 0, 0
      0, 0, 1
      1, 1, 0
      > 2
      ? Flip the first two columns, the last two rows now count.
  """

def p20(explain=True, n=15):
  # temperature is in Kelvin (max necessary for randint gen.)
  max_temp = 100

  out, mrs, tbs = [0]*n, {}, 0
  sam = [randint(0, max_temp) for _ in range(n)] # our temperature samples

  print()
  print("Problem 19")
  if explain:
    print(f"For example, a list of {n} elements might be: ")
  print()
  print(f" {astr(sam)}")
  print()
  input("Press enter/return to see the result: ")

  print()

  # the actual algo, only goes over once with constant time lookups
  for i, t in enumerate(sam[::-1]):
    t = int(t)
    tbs &= ~(2**(t+1) - 1)
    bit = tbs & -tbs
    if bit: out[n - i - 1] = i - mrs[int(log2(bit))]
    mrs[t] = i
    tbs |= 2**t

  print(f" {astr(out)}")

problems = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p20]