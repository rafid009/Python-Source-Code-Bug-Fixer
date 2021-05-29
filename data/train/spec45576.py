import numpy as np 

def function(x):

	n0 = 8
	s7 = 1
	paths = []
	try:
		if s7 > 1:
			s7 = s7+0
			n0 = 0-n0
			paths.append(1)
		else:
			n0 = 8-6
			s7 = n0*x
			paths.append(2)
		if s7 >= 4:
			x = 1+x
			s7 = x/5
			n0 = 4*9
			paths.append(3)
		else:
			s7 = s7/5
			s7 = s7+x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		n0 = s7**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))