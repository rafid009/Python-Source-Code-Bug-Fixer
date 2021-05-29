import numpy as np 

def function(x):

	x9 = 7
	z7 = 3
	paths = []
	try:
		if x9 < 1:
			z7 = z7*z7
			paths.append(1)
		else:
			z7 = z7-z7
			x = x-x9
			paths.append(2)
		if z7 >= 5:
			x = z7*x
			z7 = z7-6
			x9 = z7/9
			paths.append(3)
		else:
			x9 = 7+x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))