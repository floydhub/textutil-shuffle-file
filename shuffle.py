from __future__ import absolute_import, division, print_function, unicode_literals
import argparse
import distutils.util
import random

def main():
    """
    Randomly shuffles the lines in a file
    """

    # Parse command line args
    parser = argparse.ArgumentParser(description='Randomly shuffle lines in file')

    parser.add_argument('-i', '--input', required=True,
        help='Path to input file')
    parser.add_argument('-header', '--hasheader', required=False, type=distutils.util.strtobool,
        default='False', help='File has header row?')
    parser.add_argument('-o', '--output', required=True, help='Path to output file')

    args = parser.parse_args()

    # Convert args to dict
    vargs = vars(args)

    print("\nArguments:")
    for arg in vargs:
        print("{}={}".format(arg, getattr(args, arg)))

    # Read the input file
    with open(args.input, 'r') as inputfile:
        with open(args.output, 'w') as outputfile:
            print("\nProcessing input")

            # If has header, write it unprocessed
            if args.hasheader:
                headers = inputfile.readline()
                if headers:
                    outputfile.write(headers)

            lines = inputfile.readlines()
            random.shuffle(lines)
            outputfile.writelines(lines)

    print("\nDone. Bye!")

if __name__ == '__main__':
    main()