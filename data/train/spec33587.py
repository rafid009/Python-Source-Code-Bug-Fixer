import numpy as np 

def function(x):

	g5 = x
	z7 = 8
	paths = []
	try:
		if x < 3:
			z7 = 9+x
			paths.append(1)
		else:
			x = x/z7
			paths.append(2)
		if g5 > 5:
			x = 2-0
			g5 = z7-1
			paths.append(3)
		else:
			z7 = z7-4
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