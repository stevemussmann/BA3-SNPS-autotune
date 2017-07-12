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

	def read_stdout(self):
		fh = open(self.fname, 'r')
		for line in fh.readlines():
			if line.startswith("logP(M):"):
				line.strip('\t\n\r')
				templist = line.split()
				self.currentM = float(templist[11].strip(',('))
				self.currentA = float(templist[13].strip(','))
				self.currentF = float(templist[14].strip(','))
				print(self.currentM, self.currentA, self.currentF)

	def determine_params(self):
		self.decision(self.currentM)
		self.decision(self.currentA)
		self.decision(self.currentF)

	def decision(self, parameter):
		if parameter > 0.45:
			self.increase()
		elif parameter < 0.35:
			self.decrease()
		else:
			print("No change needed")

	def increase(self):
		print("Increase")

	def decrease(self):
		print("Decrease")


#next(x[0] for x in enumerate(L) if x[1] > 0.7)


