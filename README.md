# passgen
Simple command-line password generator because I'm lazy. 
Requires Python 3.x. Make sure to give the script correct file permissions before running.<br />

To use bash script:
```
Usage: ./passgen [-h] [-a] [-d] [-s] [-x EXCLUDE] [-n <length>]

Generate random passwords.

positional arguments:
  length             length of the password

optional arguments:
  -h          show this help message and exit
  -a          include alphabet, (default: -ads)
  -d          include digits, (default: -ads)
  -s          include special symbols (default: -ads)
  -n          length of password (default: 12)
  -x EXCLUDE  exclude any symbols in EXCLUDE enclosed with double
              quotes ex: -x "!21", make sure to escape double quotes 
              if you want to exclude them \" (default: None)
```

To use python script:
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
For example:
```
$ chmod +x passgen.py
$ chmod +x passgen
$ ./passgen -n 10
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

$ ./passgen -a
NdwyAaNaObIM 	 ZkNpjgQwmvbP
BvLVgFDWfYgM 	 DetJhfTBsCqa
fKyhmIaPLLfb 	 RYrlZJjqsnwA
SsyLzpVQxbeg 	 sPwTqJcUDgoY
LwjMXRlZkHAm 	 yssndMizuvtH
FpHJWAcHFLyJ 	 ORPCJpecldGi
hEOwQdvpZyXX 	 zolobMAdbPiy
flrKLBZFqzmh 	 cyRmdWjmPNeY
MAQsjFFHJHFg 	 GapaIVlNdaiN
UxIhHZrVRfLB 	 FCQdPvNVlxkO

$ ./passgen -ad -x 'abcdefghijklmnopqrstuvwxyz' -n 20
9I2O72J0NJ14P9S9M11N 	 29388L2556L33510UR40
9217M240X869712453M7 	 R36JV55G1437510M40C0
8H796334555LU8232W5W 	 KZQRIORFBOJVONKFPD6Q
AXPBUJATBIZWE524HZMJ 	 QX6YLWLPWSA6GFTHKV5S
Y65HG1WNF5DYR85RM5XX 	 9VN262W0563591848530
6L100O8L31F55M0Y13X2 	 56NB952NU4R139MVHX99
6846PXS9TEN0M45424C1 	 Y9673086X55888S29397
V0F794O7L427413380YV 	 4U644238642006GEP4IW
R31HZ7JEFYFAJ5Y0VTLC 	 76UU0G6JV5FX62X1D76V
U00850L6N32390680V1K 	 NJYO2QCWBGYVTIDGRIZP
```
Similarly
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
