import numpy as np 

def function(x):

	z5 = 8
	k7 = 0
	paths = []
	try:
		if k7 <= 7:
			x = x+0
			z5 = k7/z5
			x = x/6
			paths.append(1)
		else:
			k7 = k7+3
			paths.append(2)
		if k7 > 3:
			k7 = z5-6
			k7 = 8+5
			paths.append(3)
		else:
			x = 8*x
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