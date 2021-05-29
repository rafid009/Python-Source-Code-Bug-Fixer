import numpy as np 

def function(x):

	z7 = x
	a4 = 3
	paths = []
	try:
		if x > 5:
			a4 = a4*3
			x = x+z7
			paths.append(1)
		else:
			z7 = x/z7
			paths.append(2)
		if z7 >= 5:
			x = z7/x
			a4 = a4*0
			paths.append(3)
		else:
			x = x-a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))