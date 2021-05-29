import numpy as np 

def function(x):

	e6 = x
	z3 = 7
	paths = []
	try:
		if x < 4:
			x = 9*x
			x = 8-x
			paths.append(1)
		else:
			x = 0+z3
			z3 = 2+5
			z3 = e6*0
			paths.append(2)
		if e6 < 9:
			z3 = 4-z3
			paths.append(3)
		else:
			e6 = 4*6
			e6 = e6-3
			e6 = e6-e6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))