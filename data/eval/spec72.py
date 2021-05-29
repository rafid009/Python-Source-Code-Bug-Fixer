import numpy as np 

def function(x):

	n4 = x
	z3 = x
	x = 2
	paths = []
	try:
		if x > 4:
			x = x/x
			z3 = z3+z3
			x = 3/x
			paths.append(1)
		else:
			z3 = z3*9
			paths.append(2)
		if x < 4:
			x = x*5
			paths.append(3)
		else:
			x = 9/7
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		n4 = z3**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))