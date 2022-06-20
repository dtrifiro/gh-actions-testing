import argparse
from sys import argv

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--foo")
parser.add_argument("--quz")

args = parser.parse_args(argv[1:])

print(f"{args.foo=}")
print(f"{args.quz=}")
