import numpy as np 

def function(x):

	z3 = x
	j5 = x
	paths = []
	try:
		if j5 > 6:
			z3 = 4+z3
			j5 = j5/2
			j5 = j5/7
			paths.append(1)
		else:
			z3 = x/3
			paths.append(2)
		if z3 > 7:
			z3 = j5-z3
			z3 = z3/x
			paths.append(3)
		else:
			x = j5+4
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