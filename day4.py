import re
import fileinput

# for testing
lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

lines = fileinput.input()

def parse(lines):
  _parse = lambda x: tuple(map(int, x.split()))
  for line in lines:
    matches = re.findall(r"Card\s+(\d+):\s+(.*)\s+\|\s+(.*)", line)
    for match in matches:
      yield int(match[0]), _parse(match[1]), _parse(match[2])

def get_winners(card):
    _, a, b = card
    return set(a).intersection(set(b))

def calc_score(cards):
  for _, winners in cards.items():
    if len(winners) == 0:
      yield 0
    else:
      yield 2**(len(winners) - 1)

cards = list(parse(lines))
winners = { card[0]: get_winners(card) for card in cards}

# part 1
print(sum(calc_score(winners)))

# part 2
queue = list(winners.keys())
collection = list(winners.keys())
while queue:
  start_queue = list(queue)
  card_id = queue.pop()
  lo = card_id + 1
  hi = lo + len(winners[card_id])
  new_cards = list(range(lo, hi))
  collection.extend(new_cards)
  queue.extend(new_cards)

print(len(collection))