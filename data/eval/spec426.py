import numpy as np 

def function(x):

	y8 = 7
	z9 = 7
	paths = []
	try:
		if x < 0:
			y8 = 6-y8
			y8 = x+8
			paths.append(1)
		else:
			y8 = 0/y8
			y8 = y8-1
			paths.append(2)
		if z9 > 3:
			z9 = 7-3
			z9 = x/7
			z9 = z9-y8
			paths.append(3)
		else:
			x = 8*x
			y8 = y8/y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))