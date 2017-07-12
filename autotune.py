from __future__ import print_function

class Autotune():
	'Class for tuning parameters to run Bayesass'
	

	def __init__(self, fname,m,a,f):
		self.fname = fname
		self.oldM = m
		self.oldA = a
		self.oldF = f
		self.currentM = float()
		self.currentA = float()
		self.currentF = float()
		self.newM = float()
		self.newA = float()
		self.newF = float()

	def read_stdout(self):
		fh = open(self.fname, 'r')
		for line in fh.readlines():
			if line.startswith("logP(M):"):
				line.strip('\t\n\r')
				templist = line.split()
				self.currentM = templist[11].strip(',(')
				self.currentA = templist[13].strip(',')
				self.currentF = templist[14].strip(',')
				print(self.currentM, self.currentA, self.currentF)
