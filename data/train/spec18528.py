import numpy as np 

def function(x):

	z7 = 8
	j9 = x
	paths = []
	try:
		if j9 <= 9:
			x = 3/x
			z7 = 2+2
			paths.append(1)
		else:
			x = 3+9
			z7 = x+9
			z7 = 9+z7
			paths.append(2)
		if z7 <= 1:
			j9 = 9+3
			x = z7+2
			x = x+x
			paths.append(3)
		else:
			j9 = j9*7
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