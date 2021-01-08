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
Make sure to give the script correct file permissions before running. For example:
```
$ chmod +x passgen.py
$ python3 passgen.py 10
[7657J91,6 	 r5fZ4$$OK2
X24~2{2873 	 ]P7RLF488q
ysm`i3N7ZA 	 2H,49W@V2c
DFn/p;msBY 	 6xM4H$-J12
661GuAYR{d 	 &nD[-\NHw^
7~/7`}z*(; 	 f3VPq4\`vp
P}f30x9754 	 07cv6jJ8n(
[{>Ufo_qC6 	 &(Hs\/jmq@
3`=@${_>}' 	 \#`mh=]D-]
8'$33)2Jf1 	 k0W4qmiVfk

$ python3 passgen.py -a 10
fmUUhLMipU 	 ZZMRDWyapo
QCRuGRTTZW 	 fjyPHTztnw
xOgWcXIYct 	 CSzoFXkHDm
kSNinHyOza 	 lVZSyeAzds
GniJLJbCko 	 JgxtKEnKeS
VzykGSkWty 	 GMyBCmqHVI
BjwQWHhspN 	 HxUeRuIJEu
OvAVjojzgO 	 MUGEbfzbSp
DShxlRuVpx 	 jSVwbjhExx
FmrEnhIFPR 	 HhEskJTiHd

$ python3 passgen.py -a --exclude 'abcdefghijklmnopqrstuvwxyz' 10
AHNCLDCYSQ 	 XTDKECXAGL
IDCAQXNQIJ 	 IXDBOLEJOC
LAVQJTCUBR 	 BSUNXMBZYD
MDUXJGPHLX 	 YMPDJWVQAC
YFRHFZYKLD 	 JFQEHUCDMA
LBCQWHAQXV 	 WPLRJLMGDZ
KHMUDFOIDY 	 BBPFEIBOJF
HRPYTPJPAA 	 HVGYDOUPTL
ULIQOTUFBI 	 OLRCBZGYQY
PEGATICTIL 	 TSVXIAJUES
```
