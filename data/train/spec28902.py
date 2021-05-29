import numpy as np 

def function(x):

	z3 = x
	j4 = x
	x = x
	paths = []
	try:
		if j4 < 8:
			x = x+8
			x = 2-x
			z3 = j4-9
			paths.append(1)
		else:
			z3 = 1+7
			x = x/4
			paths.append(2)
		if z3 < 7:
			x = x-3
			j4 = 4/j4
			j4 = j4-7
			paths.append(3)
		else:
			z3 = z3/3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))