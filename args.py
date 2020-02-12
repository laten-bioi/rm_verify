import argparse
import sys

def get_args():
    parse = argparse.ArgumentParser(description='Process args for rm_verify')
    parse.add_argument(
        '-i', help='Input directory containing element family files')
    parse.add_argument(
        '-c', default=False, help='Run program from collection of cluster files')
    parse.add_argument('-o', help='Outpur directory where results are written')
    parse.add_argument(
        '-b', help='Path to blast nucl database for tblastx search')
    parse.add_argument('-t', default=1, help='Number of threads to use')

    parse = parse.parse_args()
    if not parse.i and not parse.c:
        print('Must specify -i or -c')
        sys.exit()
    if not parse.o:
        print('Must give path to an output directory')
        sys.exit()

    return parse
