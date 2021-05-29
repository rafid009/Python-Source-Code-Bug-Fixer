import numpy as np 

def function(x):

	b9 = 7
	z3 = 8
	paths = []
	try:
		if x > 5:
			z3 = 1-9
			x = x/8
			paths.append(1)
		else:
			b9 = 5/z3
			b9 = 9*4
			z3 = z3*x
			paths.append(2)
		if x <= 8:
			b9 = b9+z3
			paths.append(3)
		else:
			x = 6*8
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))