import numpy as np 

def function(x):

	u4 = 4
	z2 = 1
	paths = []
	try:
		if z2 < 3:
			x = 9*x
			paths.append(1)
		else:
			x = x*7
			z2 = z2/2
			x = u4+x
			paths.append(2)
		if u4 < 9:
			u4 = u4+2
			z2 = 5/3
			z2 = x-3
			paths.append(3)
		else:
			z2 = u4/z2
			x = 9*z2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))