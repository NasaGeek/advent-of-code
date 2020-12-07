from d2 import inp

import re

def main():
    for line in inp.split("\n"):
        low, high, letter, password = re.match(r"([0-9]+)-([0-9]+) (.): (.*)", line).groups()
        low = int(low) - 1
        high = int(high) - 1
        yield (password[low] == letter) ^ (password[high] == letter)

if __name__ == '__main__':
    print(sum(main()))
