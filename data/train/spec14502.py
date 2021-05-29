import numpy as np 

def function(x):

	l3 = x
	z4 = 2
	paths = []
	try:
		if l3 < 1:
			x = 4-l3
			z4 = z4*2
			paths.append(1)
		else:
			z4 = 7-x
			paths.append(2)
		if l3 < 0:
			x = x/6
			x = x*3
			paths.append(3)
		else:
			z4 = x+0
			x = 6-x
			x = 4-6
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