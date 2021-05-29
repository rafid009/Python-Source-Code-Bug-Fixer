import numpy as np 

def function(x):

	z4 = x
	x8 = x
	paths = []
	try:
		if x < 5:
			x8 = x8+0
			paths.append(1)
		else:
			x = 5+1
			paths.append(2)
		if x8 < 7:
			x8 = 1-x
			z4 = z4-1
			paths.append(3)
		else:
			x8 = x8+8
			x = x*x
			x8 = x8+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))