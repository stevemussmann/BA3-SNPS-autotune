#!/usr/bin/env python

from comline import ComLine
from bayesass import Bayesass

import sys

def main():
	input = ComLine(sys.argv[1:])
	ba = Bayesass(input.args.immanc, input.args.loci, input.args.out)
	command = ba.create_command()
	ba.run_program(command)

main()

raise SystemExit
