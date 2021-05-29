import numpy as np 

def function(x):

	a7 = 6
	z8 = x
	paths = []
	try:
		if x <= 2:
			x = 7+1
			x = z8*2
			paths.append(1)
		else:
			z8 = z8+x
			x = a7/a7
			a7 = a7-2
			paths.append(2)
		if a7 <= 7:
			z8 = 0-z8
			a7 = a7*3
			a7 = x+a7
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))