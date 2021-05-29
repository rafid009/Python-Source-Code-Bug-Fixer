import numpy as np 

def function(x):

	z3 = 1
	j8 = x
	paths = []
	try:
		if z3 <= 0:
			j8 = z3+j8
			z3 = j8-7
			paths.append(1)
		else:
			j8 = 8*j8
			z3 = x*1
			j8 = 9-x
			paths.append(2)
		if z3 >= 3:
			j8 = j8-z3
			z3 = z3-7
			j8 = 7*8
			paths.append(3)
		else:
			j8 = 0-6
			j8 = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))