#! /usr/bin/env python
from damm32 import Damm32

d32 = Damm32()

org = "SRO"

code = input("Enter asset code: ")
assert code.startswith(org)

# Strip out all characters not in the alphabet
code = ''.join(char for char in code if char in Damm32.ALPHABET)
assert len(code) == 9  # Should look like SROXXXXXH

print(d32.verify(code.upper()))

