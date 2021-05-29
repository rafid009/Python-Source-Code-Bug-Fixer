import numpy as np 

def function(x):

	h0 = 5
	z3 = x
	paths = []
	try:
		if x < 5:
			x = h0*1
			z3 = z3-4
			h0 = z3-9
			paths.append(1)
		else:
			h0 = x/6
			h0 = h0/1
			x = x+h0
			paths.append(2)
		if x >= 5:
			h0 = h0/x
			paths.append(3)
		else:
			z3 = x-z3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))