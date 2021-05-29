import numpy as np 

def function(x):

	z3 = x
	e9 = x
	x = 4
	paths = []
	try:
		if x < 1:
			e9 = e9*e9
			z3 = z3+8
			x = 5/1
			paths.append(1)
		else:
			z3 = z3/9
			paths.append(2)
		if z3 <= 4:
			z3 = x*6
			z3 = 2+z3
			paths.append(3)
		else:
			z3 = e9-e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))