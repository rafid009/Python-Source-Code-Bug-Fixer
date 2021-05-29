import numpy as np 

def function(x):

	z3 = 6
	j4 = 5
	paths = []
	try:
		if j4 < 9:
			j4 = 1-z3
			paths.append(1)
		else:
			z3 = z3+z3
			x = j4/z3
			j4 = 2*4
			paths.append(2)
		if j4 < 8:
			x = x/z3
			j4 = 1-z3
			paths.append(3)
		else:
			x = z3*1
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))