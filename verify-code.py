#! /usr/bin/env python
from damm32 import Damm32

d32 = Damm32()

org = "SRO"

code = input("Enter asset code: ")

print(d32.verify(org + code.upper()))

