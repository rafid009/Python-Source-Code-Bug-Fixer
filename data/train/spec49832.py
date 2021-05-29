import numpy as np 

def function(x):

	z3 = x
	x1 = x
	paths = []
	try:
		if x < 0:
			z3 = 8+z3
			paths.append(1)
		else:
			z3 = z3+7
			x1 = 7-z3
			x1 = x1/9
			paths.append(2)
		if x > 6:
			x1 = 4+x1
			x1 = x+x1
			z3 = z3+7
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x1 = z3**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))