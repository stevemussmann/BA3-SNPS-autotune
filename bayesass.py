from __future__ import print_function

import subprocess
import sys

class Bayesass():
	'Class for running the program Bayesass'
	

	def __init__(self, fname, loci, out):
		self.fname = fname
		self.loci = loci
		self.out = out
		self.m = 0.1
		self.a = 0.1
		self.f = 0.1
		self.i = 10000
		self.b = 1000

	def run_program(self,string):
		print(string)
		try:
			process = subprocess.Popen(string, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			output, err = process.communicate()
			self.write_stdout(1,output)
		except:
			print("Unexpected error:")
			print(sys.exec_info())
			raise SystemExit

	def create_command(self):
		ba_command = "BA3-SNPS -F " + self.fname + \
				" -l " + str(self.loci) + \
				" -i " + str(self.i) + \
				" -b " + str(self.b) + \
				" -m " + str(self.m) + \
				" -a " + str(self.a) + \
				" -f " + str(self.f) + \
				" -o " + self.out + \
				" -t -v -g -u"
		return ba_command

	def write_stdout(self,runid,stdout):
		fn = self.fname + "." + str(runid) + ".stdout"
		fh = open(fn, 'w')
		fh.write(stdout)
		fh.close()
