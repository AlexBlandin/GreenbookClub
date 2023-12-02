# Based on the num2words package, I just simplified it https://pypi.org/project/num2words/
class Num2Word:
  high_numwords = (
    ["cent"]
    + list(
      reversed(
        [
          u + t
          for t in ["dec", "vigint", "trigint", "quadragint", "quinquagint", "sexagint", "septuagint", "octogint", "nonagint"]
          for u in ["", "un", "duo", "tre", "quattuor", "quin", "sex", "sept", "octo", "novem"]
        ]
      )
    )
    + ["non", "oct", "sept", "sext", "quint", "quadr", "tr", "b", "m"]
  )

  mid_numwords = [
    (1000, "thousand"),
    (100, "hundred"),
    (90, "ninety"),
    (80, "eighty"),
    (70, "seventy"),
    (60, "sixty"),
    (50, "fifty"),
    (40, "forty"),
    (30, "thirty"),
  ]
  low_numwords = [
    (20, "twenty"),
    (19, "nineteen"),
    (18, "eighteen"),
    (17, "seventeen"),
    (16, "sixteen"),
    (15, "fifteen"),
    (14, "fourteen"),
    (13, "thirteen"),
    (12, "twelve"),
    (11, "eleven"),
    (10, "ten"),
    (9, "nine"),
    (8, "eight"),
    (7, "seven"),
    (6, "six"),
    (5, "five"),
    (4, "four"),
    (3, "three"),
    (2, "two"),
    (1, "one"),
    (0, "zero"),
  ]
  cards = {}

  def __init__(self):
    if not len(Num2Word.cards):
      mx = 3 + 3 * len(Num2Word.high_numwords)
      for n, word in zip(range(mx, 3, -3), Num2Word.high_numwords):
        Num2Word.cards[10**n] = word + "illion"
      for n, word in Num2Word.mid_numwords:
        Num2Word.cards[n] = word
      for n, word in Num2Word.low_numwords:
        Num2Word.cards[n] = word
      Num2Word.MAXVAL = 1000 * list(self.cards.keys())[0]

  def splitnum(self, value):
    for elem in self.cards:
      if elem > value:
        continue

      out = []
      if value == 0:
        div, mod = 1, 0
      else:
        div, mod = divmod(value, elem)

      if div == 1:
        out.append((self.cards[1], 1))
      else:
        out.append(self.splitnum(div))

      out.append((self.cards[elem], elem))
      if mod:
        out.append(self.splitnum(mod))

      return out

  def clean(self, val):
    out = val
    while len(val) != 1:
      out = []
      left, right = val[:2]
      if isinstance(left, tuple) and isinstance(right, tuple):
        ltext, lnum = left
        rtext, rnum = right
        if lnum == 1 and rnum < 100:
          out.append((rtext, rnum))
        elif 100 > lnum > rnum:
          out.append((f"{ltext}-{rtext}", lnum + rnum))
        elif lnum >= 100 > rnum:
          out.append((f"{ltext} and {rtext}", lnum + rnum))
        elif rnum > lnum:
          out.append((f"{ltext} {rtext}", lnum * rnum))
        else:
          out.append((f"{ltext}, {rtext}", lnum + rnum))
        if val[2:]:
          out.append(val[2:])
      else:
        for elem in val:
          if isinstance(elem, list):
            if len(elem) == 1:
              out.append(elem[0])
            else:
              out.append(self.clean(elem))
          else:
            out.append(elem)
      val = out
    return out[0]

  def to_cardinal(self, value):
    out = ""
    if value < 0:
      value, out = abs(value), "minus "

    if value >= self.MAXVAL:
      raise OverflowError(f"abs({value}) must be less than {self.MAXVAL}.")

    words, _ = self.clean(self.splitnum(value))
    return out + words


def num2words(number):
  return Num2Word().to_cardinal(number)


if __name__ == "__main__":
  print(num2words(127486))
  print(num2words(-127486))
