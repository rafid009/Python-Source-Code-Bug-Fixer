import numpy as np 

def function(x):

	r7 = x
	z5 = 8
	paths = []
	try:
		if z5 >= 1:
			z5 = 0*z5
			x = z5+x
			paths.append(1)
		else:
			x = x+7
			x = x/r7
			paths.append(2)
		if r7 < 7:
			z5 = z5-3
			paths.append(3)
		else:
			x = 8+r7
			z5 = 4+r7
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))