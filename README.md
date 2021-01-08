# passgen
Simple command-line password generator because I'm lazy. 
Requires Python 3.x
```
usage: python3 passgen.py [-h] [-a] [-d] [-s] [--exclude EXCLUDE] length

Generate random passwords.

positional arguments:
  length             length of the password

optional arguments:
  -h, --help         show this help message and exit
  -a, --alpha        include "a-zA-Z", (default: -ads)
  -d, --digit        include "0-9", (default: -ads)
  -s, --special      include !"#$%&'()*+,-./:;<=>?@ [\]^_`{|}~ (default: -ads)
  --exclude EXCLUDE  exclude any symbols in EXCLUDE enclosed with single
                     quotes ex: '!21', (default: None)
```
