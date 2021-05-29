import numpy as np 

def function(x):

	z8 = x
	a1 = x
	paths = []
	try:
		if x < 5:
			x = x*x
			a1 = a1/7
			a1 = a1/9
			paths.append(1)
		else:
			x = 3-x
			x = z8/x
			paths.append(2)
		if a1 >= 4:
			x = x*7
			a1 = x+4
			z8 = 3-0
			paths.append(3)
		else:
			z8 = 6-7
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))