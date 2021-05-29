import numpy as np 

def function(x):

	x0 = 7
	z3 = x
	paths = []
	try:
		if x <= 5:
			x = x0+7
			paths.append(1)
		else:
			x = z3+7
			x = x/z3
			z3 = 4/z3
			paths.append(2)
		if x < 7:
			x0 = x0+6
			x = x0+7
			z3 = z3+1
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x0 = z3**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))