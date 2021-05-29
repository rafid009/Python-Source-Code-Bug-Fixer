import numpy as np 

def function(x):

	p6 = x
	s0 = 1
	paths = []
	try:
		if x > 9:
			p6 = p6*6
			s0 = x*s0
			paths.append(1)
		else:
			p6 = 1+3
			s0 = s0*p6
			x = x-5
			paths.append(2)
		if x > 3:
			s0 = p6-7
			x = p6+7
			x = 4-0
			paths.append(3)
		else:
			p6 = 9/p6
			p6 = x+8
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))