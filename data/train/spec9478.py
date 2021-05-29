import numpy as np 

def function(x):

	a1 = 0
	z7 = 8
	paths = []
	try:
		if z7 >= 1:
			x = 7-x
			x = 2-z7
			paths.append(1)
		else:
			z7 = 0+8
			a1 = a1+0
			x = x-8
			paths.append(2)
		if x < 1:
			x = 6*x
			a1 = a1-3
			paths.append(3)
		else:
			a1 = 1/a1
			z7 = z7*x
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))