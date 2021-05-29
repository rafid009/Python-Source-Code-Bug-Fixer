import numpy as np 

def function(x):

	s0 = x
	z3 = 2
	paths = []
	try:
		if x > 4:
			s0 = 3/s0
			s0 = 3*x
			x = z3-x
			paths.append(1)
		else:
			z3 = 2/z3
			x = 3+z3
			x = x*1
			paths.append(2)
		if x < 7:
			x = 3-s0
			x = 8/x
			x = s0+s0
			paths.append(3)
		else:
			z3 = x/x
			z3 = z3+4
			x = x-5
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))