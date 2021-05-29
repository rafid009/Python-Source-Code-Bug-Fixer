import numpy as np 

def function(x):

	h7 = x
	z3 = x
	paths = []
	try:
		if x <= 1:
			h7 = h7-9
			paths.append(1)
		else:
			h7 = h7/3
			x = z3+h7
			z3 = z3*z3
			paths.append(2)
		if z3 <= 9:
			x = x+3
			h7 = h7-z3
			paths.append(3)
		else:
			x = x+3
			x = 8-8
			h7 = h7+h7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		z3 = h7**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))