import numpy as np 

def function(x):

	e1 = x
	z1 = x
	paths = []
	try:
		if z1 >= 5:
			z1 = z1-0
			x = 5/x
			paths.append(1)
		else:
			x = 3-x
			e1 = 3*e1
			paths.append(2)
		if z1 < 3:
			e1 = e1/5
			paths.append(3)
		else:
			e1 = e1/e1
			x = x-z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))