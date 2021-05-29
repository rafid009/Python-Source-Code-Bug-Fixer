import numpy as np 

def function(x):

	z6 = x
	e4 = x
	paths = []
	try:
		if e4 >= 5:
			e4 = e4*e4
			z6 = z6/2
			x = 0-7
			paths.append(1)
		else:
			z6 = z6-1
			paths.append(2)
		if z6 <= 6:
			e4 = 8+x
			paths.append(3)
		else:
			e4 = 1*x
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))