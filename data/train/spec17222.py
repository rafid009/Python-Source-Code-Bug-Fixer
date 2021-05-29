import numpy as np 

def function(x):

	z4 = 9
	r4 = 5
	paths = []
	try:
		if z4 <= 3:
			x = 0+r4
			paths.append(1)
		else:
			z4 = x-r4
			paths.append(2)
		if x < 9:
			z4 = x-r4
			r4 = 8+r4
			x = x-r4
			paths.append(3)
		else:
			x = 1/r4
			x = x+6
			z4 = z4+x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		r4 = z4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))