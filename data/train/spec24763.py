import numpy as np 

def function(x):

	z4 = 5
	r8 = x
	x = x
	paths = []
	try:
		if z4 < 1:
			z4 = x/r8
			r8 = 8-z4
			paths.append(1)
		else:
			z4 = x-4
			z4 = 3*z4
			x = 9+3
			paths.append(2)
		if r8 <= 3:
			r8 = r8/x
			paths.append(3)
		else:
			z4 = 7/3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		r8 = z4**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))