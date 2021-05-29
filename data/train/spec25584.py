import numpy as np 

def function(x):

	z3 = x
	z9 = 6
	paths = []
	try:
		if x <= 4:
			z9 = z9*2
			paths.append(1)
		else:
			z9 = z9/z9
			x = x*x
			paths.append(2)
		if x >= 6:
			z3 = z3-1
			z9 = 8*z9
			paths.append(3)
		else:
			z9 = 6+3
			z3 = 0+z3
			x = 9*3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))