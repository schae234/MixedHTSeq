#!/usr/bin/env python2.7

from __future__ import print_function

import sys
import pandas as pd

import argparse


def main(args):
    pd.concat(
        [pd.read_table(x,sep='\t') for x in args.files]
    ).pivot('feature','sample',values=args.count)\
    .to_csv(args.out,sep='\t',index_label=False)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Combine fpkm from mixed_count script into table'
    )
    parser.add_argument(
        '--files',nargs='+',help='count files from mixed_count script'
    )
    parser.add_argument(
        '--count',type=str,help='which count column to use from the count file'
    )
    parser.add_argument(
        '--out',type=str,help='output file name'
    )
    args = parser.parse_args()
    # simple exit strategy
    sys.exit(main(args))
