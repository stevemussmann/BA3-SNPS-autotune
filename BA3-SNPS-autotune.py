#!/usr/bin/env python

from comline import ComLine
from autotune import Autotune
from bayesass import Bayesass

import sys

def main():
	input = ComLine(sys.argv[1:])
	ba = Bayesass(input.args.immanc, input.args.loci, input.args.out)
	for i in xrange(1, input.args.reps+1, 1):
		command = ba.create_command()
		stdout = ba.run_program(command,i)
		tune = Autotune(stdout,ba.m,ba.a,ba.f)
		tune.read_stdout()

main()

raise SystemExit
