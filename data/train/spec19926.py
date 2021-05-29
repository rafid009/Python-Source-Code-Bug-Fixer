import numpy as np 

def function(x):

	h2 = 1
	z3 = x
	paths = []
	try:
		if z3 <= 7:
			h2 = h2*5
			z3 = x+1
			z3 = z3+5
			paths.append(1)
		else:
			h2 = z3/z3
			paths.append(2)
		if h2 <= 2:
			z3 = 9+4
			x = 1+z3
			x = x-6
			paths.append(3)
		else:
			h2 = z3-h2
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))