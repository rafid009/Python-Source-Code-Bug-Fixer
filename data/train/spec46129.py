import numpy as np 

def function(x):

	a4 = 4
	z7 = 0
	paths = []
	try:
		if a4 >= 8:
			x = 0+x
			z7 = 3-2
			a4 = a4-z7
			paths.append(1)
		else:
			x = 1+7
			paths.append(2)
		if a4 <= 3:
			x = x/a4
			paths.append(3)
		else:
			a4 = a4-6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		z7 = a4**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))