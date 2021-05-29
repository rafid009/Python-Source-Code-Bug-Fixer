import numpy as np 

def function(x):

	z4 = x
	r8 = x
	paths = []
	try:
		if z4 < 9:
			r8 = x+6
			paths.append(1)
		else:
			r8 = r8+r8
			z4 = z4*6
			x = r8/x
			paths.append(2)
		if r8 < 2:
			z4 = 5+7
			paths.append(3)
		else:
			z4 = z4-6
			r8 = r8-0
			x = 9*z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))