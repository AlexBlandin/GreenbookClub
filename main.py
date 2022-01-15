from math import log10, log2, ceil, floor, sqrt
from collections import defaultdict
from random import randint, sample
from itertools import combinations
from pathlib import Path
from cmd import Cmd
import os

from BalancedTernary import BalancedTernary as tern
from num2words import num2words

def join(arr, sep=" ", blocky=False): # str.join only takes list[str]
  if blocky: return "".join(["█" if a else " " for a in arr])
  else: return sep.join([str(a) for a in arr])

def name(p: callable) -> str: return next(filter(None, p.__doc__.splitlines())).strip()

history = defaultdict(dict)

def clean(s: str) -> str: return s.replace("!","").replace(",","").replace(":","")

def pprintout(p: callable, example_text: str, example: str, *result):
  """Standard interactive printout for a problem"""
  global history
  history[clean(name(p))][example] = result
  print(name(p))
  print(example_text)
  print("", example)
  print()
  input("Press enter/return to see the result: ")
  print("", *result)
  print()

def pprintoutplus(p: callable, extension: str, example_text: str, example: str, *result):
  """Standard interactive printout for an extended problem"""
  global history
  history[clean(f"{name(p)} {extension}")][example] = result
  input(f"Press enter/return to see the extended problem: ")
  print(name(p), extension)
  print(example_text)
  print("", example)
  print()
  input("Press enter/return to see the result: ")
  print("", *result)
  print()

def parse(arg: str, default: int): return int(arg) if arg.isdecimal() else default

class Greenbook(Cmd):
  intro = """
   ██████╗ ██████╗ ███████╗███████╗███╗   ██╗  ██████╗  ██████╗  ██████╗ ██╗  ██╗
  ██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║  ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
  ██║  ███╗██████╔╝█████╗  █████╗  ██╔██╗ ██║  ██████╔╝██║   ██║██║   ██║█████╔╝
  ██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║  ██╔══██╗██║   ██║██║   ██║██╔═██╗
  ╚██████╔╝██║  ██║███████╗███████╗██║ ╚████║  ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
  
   ██████╗██╗     ██╗   ██╗██████╗
  ██╔════╝██║     ██║   ██║██╔══██╗
  ██║     ██║     ██║   ██║██████╔╝
  ██║     ██║     ██║   ██║██╔══██╗
  ╚██████╗███████╗╚██████╔╝██████╔╝
   ╚═════╝╚══════╝ ╚═════╝ ╚═════╝
  
  Welcome to Greenbook Club!
  
  Please select a problem by typing its name, type "help" or "?" for the list of
  problems, or type "help problem" for a specific problem to get its description
  and any examples. You can add a value n for the size of the problem, such as
  "problem 15"... I recommend you don't go too large, since terminals tend to
  make a messy printout with large n. Type "history" to get all previous example
  and answer pairs as per-problem .json files.
  """
  prompt = "📗 " if os.name != "nt" else "📗  "
  
  def default(self, args):
    args = args.split()
    for i in range(1, len(args)+1):
      as_arg = "_".join(["do"]+args[:i])
      if hasattr(self, as_arg):
        f = getattr(self, as_arg)
        if callable(f): f(" ".join(args[i:])) # just guard against "prompt" etc
  
  def do_exit(self, *_):
    """What do you think it does?"""
    return True
  
  def do_history(self, *_):
    """Prints the history of examples to problem-specific output files (extensions are counted as separate)"""
    global history
    if not Path("./examples/").exists(): Path("./examples/").mkdir() # os.mkdir("./examples/")
    for prob, pairs in history.items():
      with open(f"examples/{prob}.txt", "w+", encoding="utf8") as f:
        for k,v in pairs.items():
          f.write(f"? {k}\n")
          print("=", *v, file=f)
          f.write("\n")
  
  def do_odds_and_evens(self, arg):
    """
    Odds and Evens!
    
    Given a list of n numbers, return a new list containing all the even elements
    of the original list, followed by all the odd elements of the original list.
    So long as it is <evens> followed by <odds>, they can be in any order.
    
      ? 51 42 43 67 46
      = 42 46 51 43 67
    
    Now, extend this by formatting your outputs, namely the output evens are in
    ascending order `(2, 4, 6)`, and the output odds are in descending order
    `(5, 3, 1)`.
    
      ? 51 42 43 67 46
      = 42 46 67 51 43
    """
    
    n = parse(arg, 20)
    biggest_number = 99 # random, so might not see
    numbers = [randint(0, biggest_number) for _ in range(n)]
    
    odd, even = lambda x: not x%2, lambda x: x%2
    odds, evens = list(filter(odd, numbers)), list(filter(even, numbers))
    
    pprintout(self.do_odds_and_evens,
              f"For example, a list of {n} elements might be: ", join(numbers),
              join(evens), join(odds)
    )
    
    # Timsort is O(n log n) at worst (merge), O(n) at best (insertion/reverse)
    # So we have best case O(n), average O(n log n/2), and worst case O(n log n)
    # Where roughly exact is O(n log nr) where r is the ratio odds : evens >=
    # 0.5 we can intuitively see the speedup, as we don't "merge" back together
    # for that final step, which is the benefit of having two disjoint halves on
    # average. Otherwise, we are bound to the larger of the two, so the
    # "significant portion" of the ratio between odds and evens (the 7 of 7:3 as
    # 0.7) gives O(n log nr).
    odds, evens = sorted(odds, reverse=True), sorted(evens)
    
    pprintoutplus(self.do_odds_and_evens, "extended",
                  f"For example, a list of {n} elements might be: ", join(numbers),
                  join(evens), join(odds)
    )
  
  def do_zerosum_game(self, arg):
    """
    Zero-Sum Game!
    
    Given a list of n integers, find all pairs that sum to zero.
    
      ? -9 3 9 0 -3
      = (9, -9) (3, -3)
    
    Now we extend this problem, finding all sets of 3 integers that sum to zero.
    
      ? 0 9 0 0 2
      = (0, 0, 0)
      
      ? -5 -4 4 7 0
      = (-4, 0, 4)
      
      ? -9 0 -3 -3 3 -5 0 0 5 2
      = (-5, 0, 5) (-5, 2, 3) (-3, 0, 3) (0, 0, 0)
    """
    
    n = parse(arg, 10)
    biggest_number = 9
    numbers = [randint(-biggest_number, biggest_number) for _ in range(n)]
    numbers = numbers + [-x for x in numbers] + [0]*randint(0,3) # bias for more 0s
    numbers = sample(sample(numbers, 2*n), n)
    
    results = []
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
        results.append(join(["(0, 0)"]*min(int(zeroes/2), 1)))
      
      for x, d in includes.items():
        m = min(d["+"], d["-"])
        if m > 0:
          results.append(join([f"({x}, {-x})"]*m))
    else:
      results.append("No pairs in the list")
    
    pprintout(self.do_zerosum_game,
              f"For example, a list of {n} elements might be: ", join(numbers),
              join(results)
    )
    
    matches = [f"({a}, {b}, {c})" for a, b, c in [tuple(combo) for combo in combinations(sorted(list(set(numbers))), 3)] if a + b + c == 0]
    if numbers.count(0) > 3: matches.append("(0, 0, 0)")
    
    pprintoutplus(self.do_zerosum_game, "extended",
                  f"For example, a list of {n} elements might be: ", join(numbers),
                  join(matches)
    )
  
  def do_lispy_business(self, arg):
    """
    Lispy Business!
    
    Given an input containing parenthesis, write a function to decide if the
    parenthesis are matched. That is, for every opening parenthesis `(` there must
    be a unique corresponding closing parenthesis `)` and vice versa.
    
      ? (()())()
      = Yes
      
      ? ()(())(())(())()
      = Yes
      
      ? (print)((Google())Green)(((Book)))
      = Yes
      
      ? d)(f(*o')F))r
      = No
      
      ? print(Book)()(())
      = Yes
      
      ? (Hello)(()(m)ain)))
      = No
      
      ? (Hello)(((int))(H)ello)(print)(())((()))
      = Yes
      
      ? ("Neaff" . ("Porth albot" . ("Brishtol Parkway" . ("Cardiff Shentral" . nil))))
      = Yes
    """
    
    n = parse(arg, 7)
    s = "" # our lispy string
    lexicon = ["Hello", "world", "main", "int", "print", "lithp", "Google", "Green", "Book"]
    
    # Lithp - definition of Lithp by The Free Dictionary (https://www.thefreedictionary.com/Lithp)
    # Lithp. n. One of the first high-level programming languages, designed to handle complex data structures.
    
    o, c, i = 0, 0, 0
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
    
    if randint(1, 3) == 1 and len(s) > 1: # corrupt that string
      if randint(1, 4) == 1: # generate a real garbled string
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
    
    pprintout(self.do_lispy_business,
              f"An example string with {n} lexical units", s,
              "Yes" if stack == 0 and matching else "No"
    )
  
  def do_door_problem(self, arg):
    """
    The Legendary Door Problem!
    
    Given 100 open doors, how many doors are left open if you were to close
    every other door, then open/close (toggle) every third door, then every
    fourth door, and so on until you open/close the final door?
    
    Now, given any n doors, how many would be left open? Can you express this as
    an equation d(n) = ???
    """
    
    n = parse(arg, 1000)
    pprintout(self.do_door_problem,
              f"For this problem, we start with exactly:", "100 doors",
              f"{floor(sqrt(100))} left open"
    )
    
    number = randint(1, n)
    pprintoutplus(self.do_door_problem, "extended",
                  f"For example, with doors <= {n}, we can have exactly:", f"{number} doors",
                  f"{floor(sqrt(number))} left open"
    )
  
  def do_deadly_soda(self, arg):
    """
    Deadly Soda!
    
    You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test
    strips which can be used to detect poison.

    A single drop of poison will turn the test strip positive permanently. 

    You can put any number of drops on a test strip at once, and you can reuse a
    test strip as many times as you'd like (as long as the results are
    negative). However, you can only run tests once per day, and it takes seven
    days to return a result.

    How would you figure out the poisoned bottle in as few days as possible?
    
    Now, does this generalise? How few days can you guarantee it will take?
    """
    
    n = parse(arg, 10)
    
    pprintout(self.do_deadly_soda,
              f"For example, with only 10 test strips, we might have:", "1000 bottles",
              "7 days"
    )
    
    b = randint(n, 2**(n+10))
    pprintoutplus(self.do_deadly_soda, "generalised",
                  f"For example, with only {n} test strips, we might have:", f"{b} bottles",
                  f"{max(1,ceil(log2(b)-n+1))*7} days"
    )
  
  def do_sorted_stacking(self, arg):
    """
    Stacking Sorted!
    Wait, other way around...
    
    Given a full stack and an empty stack, how can you sort the first stack
    (smallest items on top) using only standard operations and the second stack?
    How fast can you go?
    
    Now, sort your full stack again, but this time you can have as many
    additional stacks as you want. Can you go faster?
    """
    
    n = parse(arg, 10)
    biggest_number = 9
    numbers = [randint(0, biggest_number) for _ in range(n)]
    numbers = sample(numbers, n)
    
    pprintout(self.do_sorted_stacking,
              f"For example, a stack of {n} items might be: ", numbers,
              sorted(numbers, reverse=True)
    )
  
  def do_binary_pals(self, arg):
    """
    (Non-)Binary Pals!
    
    Given an even positive integer, print the next smallest and next largest
    numbers that have the same number of 1 bits in their binary representation.
    
    Now, what if you only assume it is a positive integer? (So not only even?)
    
    Now... do you want to try this in ternary? Same number of 1s as before, but
    now you have 2s or -1s if you want --- balanced or unbalanced, you choose!
    (I recommend balanced, it's the nicer system...)
    """
    
    n = parse(arg, 5)
    number = [1]*n + [0]*int(n*0.5) # optional fudge factor for num 0s != 1s
    number = "".join([str(c) for c in (sample(number, len(number)) + [0])])
    number = int(number, 2) # base-2
    
    is_pow2 = lambda x: x and not (x & (x - 1)) # example to get people thinking
    assert not is_pow2(0) # 0 is not a power of 2 (2**-inf=0.0, but not bitwise)
    assert not is_pow2(3) # 3 is not a power of 2
    assert is_pow2(8)     # 8 is the 4th power of 2
    
    higher = lambda x: ((x | (x-1))+1) | x ^ (x & -x)
    lower = lambda x: ((x&-x)^x)|((x&-x)>>1)
    
    def lower_even(x):
      bit = x & -x     # the smallest bit
      sft = bit >> 1   # even smaller
      rid = x ^ bit    # get rid of original bit
      return rid | sft # place in shifted bit

    def higher_even(x):
      tgt = x | (x - 1)  # set all before first 1 to 1s
      tgt = tgt + 1      # +1 carries to lowest 0, makes it 1, 0s all lower
      iso = tgt & -tgt   # isolate the tgt (redundant, doing to "simplify")
      rid = x ^ (x & -x) # get rid of original bit (inlined from lower)
      return iso | rid   # place in isolated bit (it's "jumped" to the left)
    
    pprintout(self.do_binary_pals,
              f"For example, a number with {n} true/1 bits might be: ", f"{number} ({number:b})",
              f"{lower(number)} < {number} < {higher(number)} ({lower(number):b} < {number:b} < {higher(number):b})"
    )
    
    number = number // 2 # since we added a 0 to number, this always works!
    
    higher = lambda x: ((x | (x-1))+1) | x ^ (x & -x) # higher is the same!
    lower = lambda x: ((x&-x)^x)|((x&-x)>>1) if not (x & 1) else ((x ^ ((((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))) & -(((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))))) | (((((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))) & -(((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1)))) >> 1))
    
    def higher_than(x):
      return higher_even(x) # that simple
    
    def lower_than(x): 
      if not ( x & 1 ):         # is even
        return lower_even(x)    # already done the work
      tgt = (x | (x - 1)) + 1   # we're going to zero them again
      new = tgt & ~(tgt & -tgt) # restart from that zero
      iso = new & -new          # because we wanted the actual next 1
      sft = iso >> 1            # move that down
      return (x ^ iso) | sft    # tldr, as above, we just ignored a bunch
    
    ordered_clean = lambda x: f"{higher_than(x):b} > {x:b} > {lower_than(x):b}"
    ordered_inline = lambda x: f"{((x | (x-1))+1) | x ^ (x & -x):b} > {x:b} > {((x&-x)^x)|((x&-x)>>1) if not (x & 1) else ((x ^ ((((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))) & -(((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))))) | (((((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1))) & -(((x | (x - 1)) + 1) & ~(((x | (x - 1)) + 1) & -((x | (x - 1)) + 1)))) >> 1)):b}"
    
    assert ordered_clean(number) == ordered_inline(number)
    
    pprintoutplus(self.do_binary_pals, "extended",
                  f"For example, a number with {n} true/1 bits might be: ", f"{number} ({number:b})",
                  f"{lower(number)} < {number} < {higher(number)} ({lower(number):b} < {number:b} < {higher(number):b})"
    )
    
    # Do Arctic Terns prefer Balanced Ternary? I hope so.
    pprintoutplus(self.do_binary_pals, "extra extended!",
                  f"For example, a number with {n} 1 trits might be: ", f"{number} ({tern(number)}, balanced)",
                  "" # TODO: this
    )
  
  def do_water_trap(self, arg):
    """
    Water Trap!

    Imagine a histogram (bar graph). Design an algorithm to compute the volume
    of water it could hold if someone poured water across the top. You can
    assume that each histogram bar has width 1. (Says "volume" but really it's
    area since 2D.)

      ? {0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0}
      = 26
    
    Can visualise the problem if you wish, the above example looks like:
    
         █
         █~~~~█
      █~~█    █
      █  █  █ █
      █  █  █ █
      █  █  █ █~█
    ---------------- (height=0) █ = solid, "~" = waterline
    0040060030501000
    """
    
    # n is the number of samples, height is ints>=0, max used for sample generation
    n, max_height = parse(arg, 10), 8 # or parse(arg, 1000000), 255

    s = [randint(0, max_height) for i in range(n)] # our heightmap
    t = [0]*n # minimum of the tallest on either side of a point
    r = 0 # how much water we trap
    peak = 0 # highest point we've seen so far

    for i, h in enumerate(s): # go over forwards
      t[i] = peak
      if h > peak: peak = h

    peak = 0 # resetting because now we're going the other way
    for i, h in enumerate(s[::-1]): # go over backwards
      if t[i] > peak: t[i] = peak
      if h > peak: peak = h
      if h < t[i]: r += t[i] - h # add any water trapped "above" this point

    pprintout(self.do_water_trap,
              f"For example, a water trap {n} long with heights:", join(s),
              f"Trapped {r} water"
    )
  
  def do_say_a_word(self, arg):
    """
    Say a word!
    Any word!
    
    Given any number in the range ±2 Billion, return it as a string of natural
    written/spoken English.
    
      ? 1234
      = one thousand, two hundred and thirty-four
      
      ? -92435
      = minus ninety-two thousand, four hundred and thirty-five
    """
    
    n = parse(arg, 0)
    if not len(arg.strip()):
      n = randint(-2 * 10**9, 2 * 10**9)
    
    pprintout(self.do_say_a_word,
              f"For example, given: ", n,
              num2words(n)
    )
  
  def do_ip_misaddress(self, arg):
    """
    IP Misaddress!

    Greenbook Club has come into possession of an old IPv4 networking system
    made by Swansea Uni researchers in the 80s (don't ask us how, John Tucker
    has his ways). The only problem is, some bright spark decided to break the
    spec, so nothing stored looks like IP addresses!

    For example, Swansea's IP is normally 137.44.1.20, however this system has
    it stored as `5mZtBU`! That's right, it's a mnemonic IP system! Completely
    out of spec, but Tucker wants us to convert these old "Swansea IP" addresses
    into normal IPv4. Handily, there's an old comment left that you can read.
    
      ? 137.44.1.20
      = 5mZtBU
      
      ? 255.0.0.1
      = 10f.A.A.B
      
      ? 48.8.9.72
      = ZxIJZ5t

    As an extension, some IP addresses in our modern table aren't in the normal
    "quad" format (like 137.44.1.20), but instead are other compatible (in-spec)
    formats! So, in order to make matching easier (because who on earth
    canonises anything) Tucker wants you to produce each address in a range of
    different formats.
    """
    
    ip = ".".join([str(randint(0,255)) for _ in range(4)])
    z_a = ord("z")-ord("a")
    sip = []
    for byte in ip.split("."):
      b, s = int(byte), []
      if b < ord("a"):
        b += ord("a")
        if b > ord("z"):
          s.append("Z")
          b -= z_a
          if b > ord("z"):
            z,b = divmod(b, z_a)
            s.append(str(z))
            s.append(chr(b+ord("a")))
          else:
            s.append(chr(b))
        else:
          s.append(chr(b).upper())
        sip.append("".join(s))
      elif b > ord("z"):
        z,b = divmod(b, z_a)
        s.append(str(z))
        s.append(chr(b+ord("a")))
        sip.append("".join(s))
      else:
        sip.append(chr(b))
    
    pprintout(self.do_ip_misaddress,
              f"For example, the SIP: ", ".".join(sip),
              ip
    )
  
  def do_calculate(self, arg):
    """
    (Shut up and) Calculate!
    
    You have a calculator that only has working addition and negation buttons (not
    subtraction, as in 4 to -4, and -4 to 4).
    
    1. Define subtraction using any or all of those two operations.
    2. Define multiplication using any or all of those two operations and
      subtraction.
    3. Define division using any or all of of those two operations, as well as
      multiplication and subtraction.
    
    (Hint, you may not need every available operations for each part.)
    """
    
    if not len(arg.strip()):
      pass # generate our own equation string
    
    pprintout(self.do_calculate,
              f"Sorry, this is still on my TODO list", "",
              "Sorry, this is still on my TODO list" # TODO: this
    )
  
  def do_magic_indices(self, arg):
    """
    Magic Indices! (Not beans...)
    
    An array a[] might have "magix indices", which is when `a[i] == i`. If it is
    unsorted, what is the most efficient algorithm?
    
    Now, what if a[] was sorted?
    """
    
    # n = parse(arg, 10)
    pprintout(self.do_magic_indices,
              f"Sorry, this is still on my TODO list", "",
              "Sorry, this is still on my TODO list" # TODO: this
    )
  
  def do_zero_the_matrix(self, arg):
    """
    Zero The Matrix!
    The Prequel?
    
    Given a matrix of sizes NxM, create a new matrix of the same size where all
    rows and columns containing a 0 in the original matrix are themselves now all
    0s.
    
    What's the complexity in both time and space of your algorithm? Can you go
    faster, or use less space? Can you do it without copying the matrix? (Don't
    try to be cheeky either.)
    
      ? 1,2,3,4
        1,0,8,7
        4,4,0,2
        6,7,8,9
        1,2,3,4
      
      = 1,0,0,4
        0,0,0,0
        0,0,0,0
        6,0,0,9
        1,0,0,4
    """
    
    # n = parse(arg, 5)
    pprintout(self.do_zero_the_matrix,
              f"Sorry, this is still on my TODO list", "",
              "Sorry, this is still on my TODO list" # TODO: this
    )
  
  def do_matrix_search(self, arg):
    """
    The Matrix: Search!
    (For Neo)
    
    Given an NxM matrix, describe an algorithm to search for a given value. The
    following properties hold for the matrix:
    
    1. Each row is comprised of integers sorted in ascending order (left to right)
    2. The first value on a given row is strictly greater than the last value of
      the row before it.
    
    For example, given:
    
      1,   3,  5,  7
      10, 11, 16, 20
      23, 30, 34, 50
    
    Then we can search for:
    
      ? 3
      = true
    
    How fast can you go? Why?
    """
    
    # n = parse(arg, 5)
    pprintout(self.do_matrix_search,
              f"Sorry, this is still on my TODO list", "",
              "Sorry, this is still on my TODO list" # TODO: this
    )
  
  def do_matrix_revolve(self, arg):
    """
    The Matrix: Revolutions!
    
    Given an N x N matrix, write a method to rotate the matrix by 90 degrees.

      ? [[1,2,3],
         [4,5,6],
         [7,8,9]]

      = [[7,4,1],
         [8,5,2],
         [9,6,3]]
    
    How fast can you go? Can you do this with O(1) space?
    """# the rotate 90 degrees / transpose one
    
    # n = parse(arg, 5)
    pprintout(self.do_matrix_revolve,
              f"Sorry, this is still on my TODO list", "",
              "Sorry, this is still on my TODO list" # TODO: this
    )
  
  def do_too_many_twos(self, arg):
    """
    Too Many Twos!
    
    Given the positive integer n < 10000, determine how many 2s appear in the
    numbers between 0 and n.
    
      ? 25
      = 9 (2, 12, 20, 21, 22, 23, 24, 25)
    
    Now, what if n is any positive integer? How fast can you go?
    """ # TODO: uhhh what is this even
    
    # n = parse(arg, 5)
    pprintout(self.do_too_many_twos,
              f"Sorry, this is still on my TODO list", "",
              "Sorry, this is still on my TODO list" # TODO: this
    )
  
  def do_top_temps(self, arg):
    """
    Top Temperatures!
    
    Given a list of daily temperatures, return a list that, for each day in the
    input, tells you how many days you would have to wait until a warmer
    temperature. If there are no future days for which this is possible, that
    day is assigned the value 0.
    
      ? 73, 74, 75, 71, 69, 72, 76, 73
      = 1,  1,  4,  2,  1,  1,  0,  0
    
    Now, can you do this in linear time? How much space does this require? Can
    you reduce that asymptotically?
    """
    
    n = parse(arg, 15)
    # temperature is in Kelvin (max necessary for randint gen.)
    max_temp = 100
    
    out, mrs, tbs = [0]*n, {}, 0
    sam = [randint(0, max_temp) for _ in range(n)] # our temperature samples
    
    # the actual algo, linear, only goes over once with constant time lookups
    for i, t in enumerate(sam[::-1]):
      t = int(t)
      tbs &= ~(2**(t+1) - 1)
      bit = tbs & -tbs
      if bit: out[n - i - 1] = i - mrs[int(log2(bit))]
      mrs[t] = i
      tbs |= 2**t
    
    pprintout(self.do_top_temps,
              f"For example, a list of {n} elements might be: ", join(sam),
              join(out)
    )
  
  def do_matrix_flip(self, arg):
    """
    The Matrix: Flip!
    
    Given a matrix consisting of 0s and 1s, we may choose any number of columns in
    the matrix and flip every cell in that column.
    
    Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.
    
    Return the maximum number of rows that have all values equal (all 1s or all
    0s) for any number of flips.
    
      ? 0, 1
        1, 1
      = 1 (No flips required, the bottom row is the only one with equal values.)
      
      ? 0, 1
        1, 0
      = 2 (Flip the first column, both rows now are consistent.)
      
      ? 0, 0, 0
        0, 0, 1
        1, 1, 0
      = 2 (Flip the first two columns, the last two rows now are consistent.)
    """
    
    # n = parse(arg, 5)
    pprintout(self.do_matrix_flip,
              f"Sorry, this is still on my TODO list", "",
              "Sorry, this is still on my TODO list" # TODO: this
    )
  
  def do_submatrix(self, arg):
    """
    The Submatrix!
    
    Given a matrix of size n*n, where the elements are either 1 or 0, find the
    largest rectangle within (submatrix) where every element is 1.
    """
    
    n = parse(arg, 10)
    matrix = [[randint(0, 1) for _ in range(n)] for _ in range(n)]
    counter = 0
    
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
    
    example = [f" #{''.join(str(i) for i in range(n))}"]
    above, rects, graveyard = [set() for _ in range(n)], {}, set()
    for j, row in enumerate(matrix):
      example.append(f"  {str(j).zfill(ceil(log10(max(n, 1))))}{join(row, blocky=True)}")
      if no_point(0, j): continue # finish early, we have the largest
      
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
                for c in range(left, i - 1): above[c].add(new_id)
              graveyard.add(rect_id) # we're killing it, so don't forget
      
      # 2nd pass, generate and preserve
      rect, left = None, None
      for i, cell in enumerate(row):
        if cell == 1:
          if left == None:
            left, fs = i, set(above[i])
            for rect_id in fs:
              counter += 1
              new_id = counter # make a new one that "inherits" the above rect
              rects[new_id] = dict(rects[rect_id])
              rects[new_id]["left"] = i
              for c in range(left, rects[new_id]["right"]+1): above[c].add(new_id)
              graveyard.add(rect_id)
          if largest != None and no_point(left, j): break # stop early
          if len(above[i] - graveyard) == 0 and rect == None: rect = {"left": left, "top": j} # new rect
        if cell == 0: # we know the bounds of this rect
          if rect == None or left == None: rect, left = None, None
          elif left != None:
            rect["right"] = i - 1 # the sequence of ones from the left
            counter += 1
            rect_id = counter
            rects[rect_id] = dict(rect)
            for c in range(left, i): above[c].add(rect_id)
            rect, left = None, None
      
      # Ended 2nd pass with a rect
      if rect != None and row[-1] != 0:
        rect["right"] = n - 1 # ended at edge
        counter += 1
        rect_id = counter
        rects[rect_id] = rect
        for c in range(left, n - 1): above[c].add(rect_id)
        rect, left = None, None
    
    results = []
    if largest != None:
      start, finish = coords(largest)
      results.append(f"The largest rectangle is from {start} to {finish}, with size {largest_size}")
      results.append("")
      results.append("  #" + "".join([str(i) for i in range(start[0],finish[0]+1)]))
      for i, row in enumerate(matrix[start[1]:finish[1]+1], start=start[1]): # just to make sure we're not crazy
        results.append(f"  {str(i).zfill(ceil(log10(max(finish[1], 1))))}{join(row[start[0]:finish[0]+1], blocky=True)}")
    else:
      results.append("There was nothing in the matrix")
    
    pprintout(self.do_submatrix,
              f"For example, a matrix of size {n}*{n} might be: ", "\n".join(example),
              "\n".join(results)
    )

if __name__ == "__main__":
  Greenbook().cmdloop()
