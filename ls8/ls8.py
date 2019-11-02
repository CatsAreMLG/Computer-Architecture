#!/usr/bin/env python3

"""Main."""

import sys
import os
from cpu import *

cpu = CPU()
path = os.path.dirname(os.path.realpath(__file__)) + '/examples/print8.ls8'

cpu.load(path)
cpu.run()
