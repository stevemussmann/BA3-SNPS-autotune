#!/usr/bin/env python
from __future__ import print_function

from comline import ComLine
from autotune import Autotune
from bayesass import Bayesass

import sys

def main():
	input = ComLine(sys.argv[1:])
	ba = Bayesass(input.args.immanc, input.args.loci, input.args.out, input.args.generations, input.args.burnin)
	for i in range(1, input.args.reps+1, 1):
		print("Running repetition",i,"of",input.args.reps)
		command = ba.create_command()
		stdout = ba.run_program(command,i)
		tune = Autotune(stdout,ba.m,ba.a,ba.f)
		tune.read_stdout()
		ba.m, ba.a, ba.f, mbool, abool, fbool = tune.determine_params(ba.testedM, ba.testedA, ba.testedF, ba.m, ba.a, ba.f)
		if all((mbool, abool, fbool)):
			earlyMessage = "Tuning completed early after " + str(i) + " rounds."
			ba.write_final_params(earlyMessage)
			raise SystemExit
	lateMessage = "Tuning not completed after " + str(input.args.reps) + " rounds."
	ba.write_final_params(lateMessage)

main()

raise SystemExit
