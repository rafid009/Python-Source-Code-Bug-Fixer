import numpy as np 

def function(x):

	z6 = 1
	x8 = 9
	paths = []
	try:
		if x < 2:
			x = x/4
			x8 = 4-x8
			paths.append(1)
		else:
			z6 = z6+9
			x8 = x*x8
			x8 = 6/3
			paths.append(2)
		if x8 < 9:
			x8 = 4/3
			paths.append(3)
		else:
			z6 = 2*6
			x8 = x8+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))