import numpy as np 

def function(x):

	z3 = 9
	e9 = x
	paths = []
	try:
		if e9 >= 7:
			e9 = 8/e9
			x = e9-x
			paths.append(1)
		else:
			x = z3/x
			paths.append(2)
		if z3 > 6:
			z3 = 8-0
			paths.append(3)
		else:
			x = x+1
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