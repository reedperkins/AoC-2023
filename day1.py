import re
import fileinput

# for testing 
lines = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split()

lines = list(fileinput.input())

def calc(lines, regex):
  parts = regex.split("|") 
  regex = f"(?=({regex}))" # ensure positive lookahead to catch overlapping words
  def transform(line):
    matches = list(map(lambda x: (parts.index(x) % 9) + 1, re.findall(regex, line)))
    to_return = int(f"{matches[0]}{matches[-1]}")
    # print(line, matches, to_return)
    return to_return
  
  return map(transform, lines)

# part 1
pattern = "1|2|3|4|5|6|7|8|9"
print(sum(calc(lines, pattern)))

# part 2
pattern = "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine"
print(sum(calc(lines, pattern)))