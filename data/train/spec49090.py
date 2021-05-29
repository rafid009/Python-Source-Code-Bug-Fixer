import numpy as np 

def function(x):

	h7 = x
	z3 = x
	paths = []
	try:
		if h7 <= 7:
			z3 = 4/z3
			paths.append(1)
		else:
			z3 = z3/9
			paths.append(2)
		if h7 < 2:
			h7 = h7+2
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		h7 = z3**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))