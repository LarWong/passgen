#!/usr/bin/env python3
"""Simple Password Generator."""

import sys
import random
import argparse
import re
from string import ascii_letters, digits, punctuation
from math import ceil
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Handle Command-line arguments
parser = argparse.ArgumentParser(description='Generate random passwords.')
parser.add_argument("-a", "--alpha",
                    help="include \"a-zA-Z\", (default: -ads)",
                    action="store_true")
parser.add_argument("-d", "--digit",
                    help="include \"0-9\", (default: -ads)",
                    action="store_true")
parser.add_argument("-s", "--special",
                    help="""include !\"#$%%&\'()*+,-./:;<=>?@
                            [\\]^_`{|}~ (default: -ads)""",
                    action="store_true")
parser.add_argument("--exclude",
                    help="exclude any symbols in EXCLUDE enclosed with single quotes ex: '!21', (default: None)")
parser.add_argument("length",
                    help="length of the password",
                    type=int)
args = parser.parse_args()

if args.length < 1:
  print("Error: unaccepted length")
  sys.exit()

decider = args.alpha or args.digit or args.special
parameters = {"conditions": ([args.alpha, args.digit, args.special] if decider
                              else 3*[True]),
              "exclude": args.exclude,
              "length": args.length
              }

def gen_one(length, reqs):
    """Generate one password with a certain length."""
    # Select 3 numbers [0, 1] uniformly that sum up to 1
    # Check : https://stackoverflow.com/questions/8064629/random-numbers-that-add-to-100-matlab/8068956#8068956
    setup = [random.random() for _ in range(0,reqs-1)] + [0, 1]
    setup.sort()
    random_ints = [ceil((setup[i+1] - setup[i])*int(length)) 
                   for i in range(0, len(setup)-1)]
    password = []
    index = 0
    # Remove any excluded symbols if necessary
    exclude_pattern = '[' + parameters["exclude"] + ']' if parameters["exclude"] else ''
    if parameters["conditions"][0]: # alpha
        mod_alpha = re.sub(exclude_pattern, '', ascii_letters)
        password += [random.choice(mod_alpha) for _ in range(0, random_ints[index])]
        index += 1
    if parameters["conditions"][1]: # digits
        mod_digit = re.sub(exclude_pattern, '', digits)
        password += [random.choice(mod_digit) for _ in range(0, random_ints[index])]
        index += 1
    if parameters["conditions"][2]: #special characters
        # used different method to translate bc regex has issues with '[]'
        mod_special = punctuation.translate(({ord(c): "" for c in parameters["exclude"]} 
                                             if parameters["exclude"] else punctuation))
        password += [random.choice(mod_special) for _ in range(0, random_ints[index])]
        index += 1
    random.shuffle(password)
    return ''.join(password[:int(length)])

# Generate 20 random passwords
reqs = parameters["conditions"].count(True)
length = parameters["length"]
for _ in range(0, 10):
    print('{} \t {}'.format(gen_one(length, reqs), gen_one(length, reqs)))
