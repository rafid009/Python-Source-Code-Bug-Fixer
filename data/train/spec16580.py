import numpy as np 

def function(x):

	z7 = 4
	y3 = x
	paths = []
	try:
		if y3 > 9:
			z7 = 4*z7
			z7 = 8+1
			paths.append(1)
		else:
			z7 = 0*z7
			paths.append(2)
		if y3 < 7:
			z7 = 5-z7
			x = x*6
			paths.append(3)
		else:
			x = x-5
			x = 8+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))