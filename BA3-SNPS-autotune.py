#!/usr/bin/env python3
#from __future__ import print_function

from comline import ComLine
from autotune import Autotune
from bayesass import Bayesass

import sys
import shutil

def cmd_exists(cmd):
	return shutil.which(cmd) is not None

def main():
	input = ComLine(sys.argv[1:])

	executable = "BA3-SNPS"

	if cmd_exists(executable) is False:
		if cmd_exists("ba3-snps") is True:
			executable = "ba3-snps"
		else:
			print("BA3-SNPS is not installed.")
			print("Please install BA3-SNPS before proceeding.")
			raise SystemExit

	ba = Bayesass(executable, input.args.immanc, input.args.loci, input.args.out, input.args.generations, input.args.burnin)
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
