import numpy as np 

def function(x):

	c5 = x
	z3 = x
	paths = []
	try:
		if c5 >= 7:
			z3 = z3-z3
			paths.append(1)
		else:
			z3 = z3*8
			z3 = z3+7
			paths.append(2)
		if c5 <= 7:
			x = c5+x
			c5 = c5+5
			c5 = 9/x
			paths.append(3)
		else:
			z3 = z3*1
			x = c5*x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		z3 = c5**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))