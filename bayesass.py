from __future__ import print_function

from decimal import *
import subprocess
import sys

class Bayesass():
	'Class for running the program Bayesass'
	

	def __init__(self, fname, loci, out, gen, burn):
		self.fname = fname
		self.loci = loci
		self.out = out
		self.m = Decimal(0.1)
		self.a = Decimal(0.1)
		self.f = Decimal(0.1)
		self.i = gen
		self.b = burn
		self.testedM = [Decimal(0), Decimal(1)]
		self.testedA = [Decimal(0), Decimal(1)]
		self.testedF = [Decimal(0), Decimal(1)]

	def run_program(self,string,i):
		print(string)
		stdout = str()
		try:
			process = subprocess.Popen(string, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			output, err = process.communicate()
			stdout = self.write_stdout(i,output)
			if process.returncode != 0:
				print("Non-zero exit status:")
				print(process.returncode)
				raise SystemExit
			print(err)
		except:
			print("Unexpected error:")
			print(sys.exec_info())
			raise SystemExit
		return stdout
		

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
		self.add_tested()
		print(self.testedM)
		print(self.testedA)
		print(self.testedF)
		return ba_command

	def add_tested(self):
		self.testedM.append(Decimal(self.m))
		self.testedA.append(Decimal(self.a))
		self.testedF.append(Decimal(self.f))

		self.testedM = sorted(self.testedM)
		self.testedA = sorted(self.testedA)
		self.testedF = sorted(self.testedF)

	def write_stdout(self,runid,stdout):
		fn = self.fname + "." + str(runid) + ".stdout"
		fh = open(fn, 'w')
		fh.write(stdout)
		fh.close()
		return fn

	def write_final_params(self,message):
		fn = self.fname + "." + "finalParams.txt"
		fh = open(fn, 'w')
		fh.write("##")
		fh.write(message)
		fh.write("\n")
		fh.write("##M\tA\tF")
		fh.write("\n")
		fh.write(str(round(self.m,4)))
		fh.write("\t")
		fh.write(str(round(self.a,4)))
		fh.write("\t")
		fh.write(str(round(self.f,4)))
		fh.write("\n")
		fh.close()
