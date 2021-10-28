from problems import problems, name

def main():
  """
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
  
  Source @ https://replit.com/@alexblandin/Greenbook-Club
  (But I don't recommend using it for your solutions.)
  """
  
  #
  # I do not recommend looking at this for optimal algorithms,
  # they're likely whatever I could write quickly to solve it.
  #

  # @greenbook and @greenbookclub seem to be available
  # post as Week-3.GreenBookClub.repl.run or something?
  # doesn't need to be on repl, though that would likely be easiest for me
  # though I saw some bad connections so either that's repl or ISS's problem

  # TODO: use docstrings to print nice problem explanations inline
  # TODO: provide a nice names for each problem rather than numeric id
  
  # Greetings
  print()
  print(main.__doc__)

  problem: callable
  nprob = len(problems)
  exit_strings = {"exit", "close", "stop", "halt", "end", "cease", "no", "back"}
  inp = input(f"Welcome to Green Book Club! Please select a Problem or ask for all <problems>: ").strip().lower()
  examples, prev_n = False, None
  
  while inp not in exit_strings:
    try:
      if not examples and inp.isdecimal() and (int(inp) < 1 or int(inp) > nprob):
        print()
        inp = input(f"Please select a Problem: ").strip().lower()
        continue
      if examples:
        inp = input("Press enter/return to see another example: ").strip().lower()
        while inp not in exit_strings:
          if inp != "" and inp.isdecimal():
            prev_n = int(inp)
            problem(False, prev_n)
          elif inp == "" and prev_n != None: problem(False, prev_n)
          elif inp == "": problem(False)
          elif inp in exit_strings: break
          else: continue
          print()
          inp = input("Press enter/return to see another example: ").strip().lower()
        examples = False
      if inp.isdecimal():
        problem = problems[int(inp)-1]
        inp = input("Please choose a value for n. If you press enter it will pick a reasonable default: ").strip().lower()
        prev_n = None
        if inp != "" and inp.isdecimal():
          if int(inp) >= 500:
            print("Please only choose REASONABLE values for n. While the program can handle it, the printout will just be messy.")
            continue
          prev_n = int(inp)
          problem(n = prev_n)
        elif inp == "": problem()
        elif inp in exit_strings: break
        else: continue
        print()
        examples = True
      elif inp == "" and problem == None:
        for p in problems: p()
      elif inp == "" and problem != None:
        problem()
      elif inp in {"problems", "all", "explain", "help"}:
        for p in problems: print(p.__doc__)
      if not examples:
        print()
        inp = input(f"Please select a Problem: ").strip().lower()
    except (KeyboardInterrupt, SystemExit):
      print()
      input("Exiting. Please press enter/return to finalise program exit. ")
      break
    except Exception as err:
      import traceback
      trace = traceback.format_exc()
      print()
      print(f"Let me know about {err}:")
      print()
      for line in str(trace).splitlines():
        print(f"   {line}")

if __name__ == "__main__":
  main()
