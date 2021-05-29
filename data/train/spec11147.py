import numpy as np 

def function(x):

	n9 = x
	s0 = x
	x = 3
	paths = []
	try:
		if x >= 1:
			x = 6+9
			x = s0*x
			paths.append(1)
		else:
			s0 = 4+9
			paths.append(2)
		if s0 < 8:
			x = s0-9
			n9 = n9-8
			n9 = 7/5
			paths.append(3)
		else:
			n9 = n9/3
			n9 = 4/n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))