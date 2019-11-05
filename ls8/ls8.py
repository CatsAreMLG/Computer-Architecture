#!/usr/bin/env python3

"""Main."""

import sys
import os
from cpu import *

cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()
