#! /usr/bin/env python
import argparse
from random import choice

from damm32 import Damm32

d32 = Damm32()

org = "SRO"

def gen_code(code='AA') -> str:
    for i in range(len(code), 5):
        code += choice(Damm32.ALPHABET)

    code += d32.calculate(org + code)
    return code


def format_code(code: str) -> str:
    if len(code) != 6:
        raise ValueError(f"Asset codes should be 6 characters long; got {code}")

    return f"{org}-{code[:3]}-{code[3:]}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate some valid SRO asset codes.",
                                     epilog="example usage: ./gen_code.py 30 --prefix AA")
    parser.add_argument("--prefix", nargs='?', default="", help="an optional prefix to fix the first 1-5 characters of the code. A 2-character prefix is recommended.")
    parser.add_argument("count", metavar='n', type=int, nargs='?', default=1, help="the number of codes to generate")

    args = parser.parse_args()
    if len(args.prefix) > 5:
        raise argparse.ArgumentTypeError("--prefix option must be 5 characters or less")
    if any(char not in d32.ALPHABET for char in args.prefix):
        raise argparse.ArgumentTypeError(f"--prefix characters must be in the Damm32 alphabet:\n{''.join(d32.ALPHABET)}")

    for _ in range(args.count):
        print(format_code(gen_code(args.prefix)))
