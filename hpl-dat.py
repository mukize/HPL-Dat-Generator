#!/usr/bin/env python3

import argparse
import math


def get_baseN(nodes, mpn):
    baseN = int(math.sqrt((mpn * 0.80 * nodes * 1024 * 1024) / 8))
    return baseN


def get_n_from_nb(baseN, nb):
    factor = int(baseN / nb)
    if factor % 2 != 0:
        factor -= 1
    realN = nb * factor
    return realN


def get_grid(nodes, ppn):
    cores = int(nodes * ppn)
    sqrt_cores = math.sqrt(cores)

    factors = []
    for num in range(2, int(sqrt_cores) + 1):
        if cores % num == 0:
            factors.append(num)
    if not factors:
        factors.append(1)

    diff = None
    keep = None
    for factor in factors:
        tmp_diff = abs(cores - factor)
        if diff is None or tmp_diff < diff:
            diff = tmp_diff
            keep = factor

    p = keep
    q = cores // keep
    return (p, q)


def calc_hpl(nodes, cpn, mpn, nb):
    baseN = get_baseN(nodes, mpn)
    realN = get_n_from_nb(baseN, nb)
    p, q = get_grid(nodes, cpn)

    contents = ""
    contents += "HPLinpack benchmark input file\n"
    contents += "Innovative Computing Laboratory, University of Tennessee\n"
    contents += "HPL.out      output file name (if any)\n"
    contents += "6            device out (6=stdout,7=stderr,file)\n"
    contents += "1            # of problems sizes (N)\n"
    contents += f"{realN}         Ns\n"
    contents += "1            # of NBs\n"
    contents += f"{nb}           NBs\n"
    contents += "0            PMAP process mapping (0=Row-,1=Column-major)\n"
    contents += "1            # of process grids (P x Q)\n"
    contents += f"{p}            Ps\n"
    contents += f"{q}            Qs\n"
    contents += "16.0         threshold\n"
    contents += "1            # of panel fact\n"
    contents += "2            PFACTs (0=left, 1=Crout, 2=Right)\n"
    contents += "1            # of recursive stopping criterium\n"
    contents += "4            NBMINs (>= 1)\n"
    contents += "1            # of panels in recursion\n"
    contents += "2            NDIVs\n"
    contents += "1            # of recursive panel fact.\n"
    contents += "1            RFACTs (0=left, 1=Crout, 2=Right)\n"
    contents += "1            # of broadcast\n"
    contents += "1            BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)\n"
    contents += "1            # of lookahead depth\n"
    contents += "1            DEPTHs (>=0)\n"
    contents += "2            SWAP (0=bin-exch,1=long,2=mix)\n"
    contents += "64           swapping threshold\n"
    contents += "0            L1 in (0=transposed,1=no-transposed) form\n"
    contents += "0            U  in (0=transposed,1=no-transposed) form\n"
    contents += "1            Equilibration (0=no,1=yes)\n"
    contents += "8            memory alignment in double (> 0)\n"
    contents += (
        "##### This line (no. 32) is ignored (it serves as a separator). ######\n"
    )
    contents += "0                               Number of additional problem sizes for PTRANS\n"
    contents += "1200 10000 30000                values of N\n"
    contents += "0                               number of additional blocking sizes for PTRANS\n"
    contents += "40 9 8 13 13 20 16 32 64        values of NB"

    return contents


def main():
    parser = argparse.ArgumentParser(
        description="A script that generate HPL dat configurations."
    )
    parser.add_argument("nodes", type=int, help="Number of nodes.")
    parser.add_argument("cpn", type=int, help="Cores per node.")
    parser.add_argument("mpn", type=int, help="Memory per node.")
    parser.add_argument("nb", type=int, help="Node block size.")

    args = parser.parse_args()
    print(calc_hpl(args.nodes, args.cpn, args.mpn, args.nb))


if __name__ == "__main__":
    main()
