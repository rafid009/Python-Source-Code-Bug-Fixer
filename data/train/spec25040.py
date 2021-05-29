import numpy as np 

def function(x):

	z3 = x
	c9 = x
	paths = []
	try:
		if c9 < 1:
			z3 = 7*z3
			c9 = 4*c9
			x = x*9
			paths.append(1)
		else:
			c9 = x+c9
			c9 = 5-3
			paths.append(2)
		if z3 < 1:
			c9 = c9+7
			paths.append(3)
		else:
			x = 5-x
			z3 = z3+c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		z3 = c9**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))