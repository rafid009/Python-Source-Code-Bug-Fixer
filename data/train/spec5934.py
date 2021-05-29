import numpy as np 

def function(x):

	z3 = x
	q8 = 1
	paths = []
	try:
		if z3 <= 2:
			q8 = 8+q8
			x = x/4
			z3 = z3+7
			paths.append(1)
		else:
			z3 = x/z3
			paths.append(2)
		if z3 < 9:
			z3 = x*1
			paths.append(3)
		else:
			q8 = q8+q8
			x = x+q8
			z3 = 2*z3
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