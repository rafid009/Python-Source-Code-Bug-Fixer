import numpy as np 

def function(x):

	z9 = 2
	z3 = x
	paths = []
	try:
		if z9 < 0:
			x = z9+x
			z3 = 0*9
			z9 = z9+0
			paths.append(1)
		else:
			x = z9-x
			paths.append(2)
		if x < 8:
			x = 5*5
			z9 = 2+z9
			z9 = 8*z3
			paths.append(3)
		else:
			z3 = x*z3
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z3 = z9**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))