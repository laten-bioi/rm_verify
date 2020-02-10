import argparse


def get_args():
    parse = argparse.ArgumentParser(description='Process args for rm_verify')
    parse.add_argument(
        '-i', help='Input directory containing element family files')
    parse.add_argument('-o', help='Outpur directory where results are written')
    parse.add_argument(
        '-b', help='Path to blast nucl database for tblastx search')
    parse.add_argument('-t', default=1, help='Number of threads to use')

    return parse
