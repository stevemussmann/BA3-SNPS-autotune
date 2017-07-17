from __future__ import print_function

import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-i", "--immanc",
							dest='immanc',
							required=True,
							help="Specify a immanc file for input."
		)
		parser.add_argument("-o", "--out",
							dest='out',
							default="output.txt",
							help="Specify an output file name."
		)
		parser.add_argument("-l", "--loci",
							dest="loci",
							type=int,
							required=True,
							help="Specify number of loci in input file"
		)
		parser.add_argument("-r", "--reps",
							dest="reps",
							type=int,
							default=15,
							help="Specify maximum number of rounds of tuning parameters"
		)
		parser.add_argument("-b", "--burnin",
							dest="burnin",
							type=int,
							default=1000,
							help="Specify burnin for Bayesass runs"
		)
		parser.add_argument("-g", "--generations",
							dest="generations",
							type=int,
							default=10000,
							help="Specify number of generations for Bayesass runs"
		)
		self.args = parser.parse_args()

		#check if files exist
		self.exists( self.args.immanc )



	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
