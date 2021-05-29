import numpy as np 

def function(x):

	s0 = x
	n0 = 2
	paths = []
	try:
		if x < 0:
			s0 = 6-s0
			s0 = 1*s0
			n0 = 3-n0
			paths.append(1)
		else:
			n0 = 5/n0
			x = x/x
			x = 7+7
			paths.append(2)
		if n0 > 5:
			s0 = s0/4
			paths.append(3)
		else:
			s0 = x-s0
			x = x-7
			s0 = 1-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))