"""
Starter code for writing a simple python cli.

At a minimum, change the name of the script, the read_data, 
transform_data, and write_data functions and away you go.

example usage:
    python myscript.py -i /path/to/input -o /path/to/output
"""
import argparse
import sys


def parse_args():

    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-i',"--in_file", type=str, help=""
                        )

    parser.add_argument('-o',"--out_file", type=str, help="",
                        default="out.tab"
                        )

    opts = parser.parse_args()
    in_file, out_file = opts.in_file, opts.out_file

    return in_file, out_file


def read_data(in_file):
    raise NotImplementedError


def data_transform(data_obj):
    raise NotImplementedError

def write_data(out_file, data_obj):
    raise NotImplementedError


def main():

    in_file, out_file = parse_args()

    data = read_data(in_file)

    new_data = data_transform(data)

    write_data(out_file, new_data)


if __name__ == "__main__":
    sys.exit(main())
