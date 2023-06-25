#! /usr/bin/env python
from random import choice

from damm32 import Damm32

d32 = Damm32()

org = "SRO"
prefix = "SB"

def gen_code(code='AA') -> str:

    for i in range(0, 3):
        code += choice(Damm32.ALPHABET)

    code += d32.calculate(org + code)
    return code

def print_code():
    code = gen_code(prefix)

    print(f"{org}-{code[:3]}-{code[3:]}")

if __name__ == "__main__":
    for _ in range(22):
        print_code()
