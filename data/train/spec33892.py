import numpy as np 

def function(x):

	u7 = x
	z3 = x
	paths = []
	try:
		if z3 >= 3:
			x = 8/x
			u7 = z3/6
			paths.append(1)
		else:
			z3 = x-z3
			z3 = 3*z3
			x = 4-x
			paths.append(2)
		if u7 > 6:
			u7 = u7*0
			u7 = 1-u7
			paths.append(3)
		else:
			x = 4*6
			z3 = z3+5
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		z3 = u7**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))