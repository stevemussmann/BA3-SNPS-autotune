from __future__ import print_function

import bisect
from decimal import *

class Autotune():
	'Class for tuning parameters to run Bayesass'
	

	def __init__(self, fname,m,a,f):
		self.fname = fname
		self.oldM = m
		self.oldA = a
		self.oldF = f
		self.currentM = Decimal()
		self.currentA = Decimal()
		self.currentF = Decimal()

	def read_stdout(self):
		fh = open(self.fname, 'r')
		for line in fh.readlines():
			if line.startswith("logP(M):"):
				line.strip('\t\n\r')
				templist = line.split()
				self.currentM = Decimal(templist[11].strip(',('))
				self.currentA = Decimal(templist[13].strip(','))
				self.currentF = Decimal(templist[14].strip(','))
				print(self.currentM, self.currentA, self.currentF)

	def determine_params(self, Mlist, Alist, Flist, M, A, F):
		newM, Mbool = self.decision(self.currentM, Mlist, M) #self.currentM = current acceptance rate for M, Mlist = previously used mixing parameter values
		newA, Abool = self.decision(self.currentA, Alist, A)
		newF, Fbool = self.decision(self.currentF, Flist, F)
		return newM, newA, newF, Mbool, Abool, Fbool

	def decision(self, accept, testedList, parameter):
		if accept > Decimal(0.45):
			return self.increase(parameter, testedList)
		elif accept < Decimal(0.35):
			return self.decrease(parameter, testedList) #parameter = current acceptance rate for parameter evaluated, testedList = previously used mixing parameter values for parameter evaluated
		else:
			return self.same(parameter, testedList)		

	def increase(self, parameter, testedList):
		print("Increase")
		element = bisect.bisect(testedList, parameter)
		#print(element)
		newP = Decimal(((testedList[element]-testedList[element-1])/2)+testedList[element-1])
		print(newP)
		return newP, False

	# may need to add safeguard to ensure negative array indices are not retrieved
	def decrease(self, parameter, testedList):
		print("Decrease")
		element = bisect.bisect(testedList, parameter)
		#print(element-2)
		newP = Decimal(testedList[element-1]-((testedList[element-1]-testedList[element-2])/2))
		print(newP)
		return newP, False

	def same(self, parameter, testedList):
		print("No change needed")
		element = bisect.bisect(testedList, parameter)
		#print(element-1)
		newP = Decimal(testedList[element-1])
		print(newP)
		return newP, True
