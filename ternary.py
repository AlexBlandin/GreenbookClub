"""
A Balanced Ternary semi-numeric class.

Not complete.

Copyright 2021 Alex Blandin
"""

from functools import reduce


class BalancedTernary:
  """
  Represented as a list of 0, 1 or -1s, with least significant digit first.

  Based on https://rosettacode.org/wiki/Balanced_ternary.
  """

  str2dig = {"1": 1, "T": -1, "0": 0}  # immutable  # noqa: RUF012
  dig2str = {1: "1", -1: "T", 0: "0"}  # immutable  # noqa: RUF012
  table = ((0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1))  # immutable

  def __init__(self, inp) -> None:  # noqa: ANN001, D107
    if isinstance(inp, str):
      self.digits = [BalancedTernary.str2dig[c] for c in reversed(inp)]
    elif isinstance(inp, int):
      self.digits = self._int2ternary(inp)
    elif isinstance(inp, BalancedTernary):
      self.digits = list(inp.digits)
    elif isinstance(inp, list):
      if all(d in {0, 1, -1} for d in inp):
        self.digits = list(inp)
      else:
        msg = "BalancedTernary: Wrong input digits."
        raise ValueError(msg)
    else:
      msg = "BalancedTernary: Wrong constructor input."
      raise TypeError(msg)

  @staticmethod
  def _int2ternary(n):  # noqa: ANN001, ANN205
    if n == 0:
      return []
    if (n % 3) == 0:
      return [0, *BalancedTernary._int2ternary(n // 3)]
    if (n % 3) == 1:
      return [1, *BalancedTernary._int2ternary(n // 3)]
    if (n % 3) == 2:  # noqa: PLR2004
      return [-1, *BalancedTernary._int2ternary((n + 1) // 3)]
    return None

  def to_int(self):  # noqa: ANN201, D102
    return reduce(lambda y, x: x + 3 * y, reversed(self.digits), 0)

  def __repr__(self) -> str:  # noqa: D105
    if not self.digits:
      return "0"
    return "".join(BalancedTernary.dig2str[d] for d in reversed(self.digits))

  @staticmethod
  def _neg(digs):  # noqa: ANN001, ANN205
    return [-d for d in digs]

  def __neg__(self):  # noqa: ANN204, D105
    return BalancedTernary(BalancedTernary._neg(self.digits))

  @staticmethod
  def _add(a, b, c=0):  # noqa: ANN001, ANN205
    if not (a and b):
      if c == 0:
        return a or b
      else:  # noqa: RET505
        return BalancedTernary._add([c], a or b)
    else:
      (d, c) = BalancedTernary.table[3 + (a[0] if a else 0) + (b[0] if b else 0) + c]
      res = BalancedTernary._add(a[1:], b[1:], c)
      # trim leading zeros
      if res or d != 0:
        return [d, *res]
      else:  # noqa: RET505
        return res

  def __add__(self, b):  # noqa: ANN001, ANN204, D105
    return BalancedTernary(BalancedTernary._add(self.digits, b.digits))

  def __sub__(self, b):  # noqa: ANN001, ANN204, D105
    return self + (-b)

  @staticmethod
  def _mul(a, b):  # noqa: ANN001, ANN205
    if not (a and b):
      return []
    else:  # noqa: RET505
      if a[0] == -1:
        x = BalancedTernary._neg(b)
      elif a[0] == 0:
        x = []
      elif a[0] == 1:
        x = b
      else:
        raise AssertionError
      y = [0, *BalancedTernary._mul(a[1:], b)]
      return BalancedTernary._add(x, y)

  def __mul__(self, b):  # noqa: ANN001, ANN204, D105
    return BalancedTernary(BalancedTernary._mul(self.digits, b.digits))


def main() -> None:  # noqa: D103
  a = BalancedTernary("1T01101")
  print("a:", a.to_int(), a)  # noqa: T201

  b = BalancedTernary(-436)
  print("b:", b.to_int(), b)  # noqa: T201

  c = BalancedTernary("1T11T")
  print("c:", c.to_int(), c)  # noqa: T201

  r = a * (b - c)
  print("a * (b - c):", r.to_int(), r)  # noqa: T201


if __name__ == "__main__":
  main()
