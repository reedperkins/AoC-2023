import re
from itertools import chain
from functools import reduce
from collections import defaultdict
import fileinput

# for testing
lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")

lines = fileinput.input()

def parse(line):
  parts = re.match(r"Game (\d+): (.*)", line) 
  return int(parts[1]), list(map(lambda hand: [tuple(x.split()) for x in hand.split(",")], parts[2].split(";")))

games = list(map(parse, lines))

# part 1

config = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def reducer(acc, pair):
  val, key = pair
  acc[key] += int(val)
  return acc

def check(game):
  _, hands = game
  for hand in hands:
    hand = reduce(reducer, hand, defaultdict(int))
    if any([hand[key] > config[key] for key in config.keys()]):
      return False
  return True

print(sum(map(lambda game: game[0], filter(check, games))))

# part 2

def max_reduce(acc, pair):
  val, key = pair
  acc[key] = max(acc[key], int(val))
  return acc

def flatten(lst):
  return list(chain.from_iterable(lst))

def num_cubes(game):
  _, hands = game
  hands = flatten(hands)
  hand = reduce(max_reduce, hands, defaultdict(int))
  return reduce(lambda x, y: x * y, hand.values())

print(sum(map(num_cubes, games)))
