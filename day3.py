import re
from collections import namedtuple
from itertools import product
import fileinput
from collections import defaultdict

# for testing
lines = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")

lines = map(lambda x: x.strip(), fileinput.input())

coord = namedtuple('Coord', ['row', 'col'])

def parse(lines):
  for i, line in enumerate(lines):
    if matches := re.finditer(r"(\d+)|([^0-9.]+)", line):
      for match in matches:
        val = list(filter(bool, match.groups()))[0]
        x1, x2 = match.span()
        span = coord(i, x1), coord(i, x2)
        type = 'num' if val.isnumeric() else 'sym'
        if type == 'num':
          val = int(val)
        yield type, val, span # part

def check_neighbor(a, b):
  a1, a2 = a
  b1, b2 = b
  return abs(a1.row - b1.row) <= 1 and (
        ((b1.col >= a1.col and b1.col <= a2.col) or
        (b2.col >= a1.col and b2.col <= a2.col))
        or
        ((a1.col >= b1.col and a1.col <= b2.col) or
        (a2.col >= b1.col and a2.col <= b2.col)))

def get_lookup(vals):
  lookup = defaultdict(set)
  for a, b in product(vals, repeat=2):
    if a != b and check_neighbor(a[2], b[2]):
      lookup[a].add(b)
  for k, v in lookup.items():
    lookup[k] = list(v)
  return lookup

vals = list(parse(lines))
lookup = get_lookup(vals)

# part 1
print(sum([k[1] for k, v in lookup.items() if k[0] == "num" and len(v) > 0]))

# part 2
print(sum([v[0][1] * v[1][1] for k, v in lookup.items() if k[1] == "*" and len(v) == 2]))