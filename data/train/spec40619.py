import numpy as np 

def function(x):

	e0 = 4
	z8 = 7
	paths = []
	try:
		if e0 <= 7:
			x = x/9
			paths.append(1)
		else:
			z8 = z8/e0
			e0 = 6+e0
			paths.append(2)
		if e0 >= 8:
			x = 7+7
			x = 0/x
			x = 5+0
			paths.append(3)
		else:
			e0 = z8+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))