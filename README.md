
# HPL.dat Generator

A python script to output an "HPL.dat" config to stdout.
Requires Python 3.

## Usage

1. Download the file:
```sh
wget https://raw.githubusercontent.com/mukize/HPL-Dat-Generator/refs/heads/main/hpl-dat.py
```

2. Make the file executable:
```sh
chmod u+x hpl-dat.py
```

3. Follow the help message:
```sh
./hpl-dat.py -h
# usage: hpl-dat.py [-h] nodes cpn mpn nb
#
# A script that generate HPL dat configurations.
#
# positional arguments:
#   nodes       Number of nodes.
#   cpn         Cores per node.
#   mpn         Memory per node.
#   nb          Node block size.
#
# options:
#   -h, --help  show this help message and exit
```
