#!/usr/bin/env python2.7
# Dont want to mess up from this
from __future__ import print_function,division

import HTSeq
import argparse
import sys
from itertools import chain


def filter_longest_transcript(gff):
    '''
        This will filter longest transcript.
    '''
    # keep buffer of passing features
    passing_features = []
    # We should buffer this because why not?
    current_gene = None
    current_mrna = None
    feature_buffer = []
    for i,ftr in enumerate(gff):
        if i % 100000 == 0:
            print("On line {}".format(i),file=sys.stderr)
        if ftr.type == 'chromosome':
            continue
        if ftr.type == 'gene':
            if current_gene is not None:
                for pfeature in [current_gene,current_mrna]+feature_buffer:
                    yield pfeature
            current_gene = ftr
            current_mrna = None
            feature_buffer = []
            
        elif ftr.type == 'mRNA':
            if current_mrna is not None:
                # test to see if feature is longer than current
                if ftr.iv.length > current_mrna.iv.length:
                    current_mrna = ftr
                    feature_buffer = []
            else:
                    current_mrna = ftr
                    feature_buffer = []
        else:
            ftr.attr['gene_id'] = current_gene.attr['Name']
            feature_buffer.append(ftr)


def main(args):
    # There ain't much to it
    if args.out == '-':
        args.out = sys.stdout
    else:
        args.out = open(args.out,'w')

    gff = HTSeq.GFF_Reader(args.gff)
    if args.mode == 'longest-transcript':
        for feature in filter_longest_transcript(gff):
            print(feature.get_gff_line(with_equal_sign=True),file=args.out,end='')
    else:
        raise ValueError('Incorrect Mode')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Filter GFF files for interesting components')
    parser.add_argument('--mode',choices=['longest-transcript'],help='Choose one of the filtering modes')
    parser.add_argument('--gff',type=str,help='The gff file to perform the filter on')
    parser.add_argument('--out',default='-',type=str,help='Output file name (default standard out)')
    args = parser.parse_args(sys.argv[1:])

    sys.exit(main(args))
