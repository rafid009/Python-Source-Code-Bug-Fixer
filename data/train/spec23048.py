import numpy as np 

def function(x):

	x5 = 8
	z2 = 0
	paths = []
	try:
		if z2 >= 8:
			x5 = x+x5
			paths.append(1)
		else:
			x = x*2
			x5 = 5-x5
			paths.append(2)
		if x <= 4:
			x5 = x5/x5
			z2 = x5/7
			x5 = 1*x
			paths.append(3)
		else:
			x5 = 0+x5
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))