import numpy as np 

def function(x):

	z7 = x
	x6 = 1
	paths = []
	try:
		if x6 >= 8:
			x6 = x+7
			x6 = z7+x6
			paths.append(1)
		else:
			x = 2+x
			x6 = 0+8
			paths.append(2)
		if x6 < 4:
			x6 = 7/z7
			paths.append(3)
		else:
			x6 = 3+x6
			z7 = 0-z7
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