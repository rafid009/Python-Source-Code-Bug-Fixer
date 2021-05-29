import numpy as np 

def function(x):

	x8 = 9
	z7 = 8
	paths = []
	try:
		if x8 > 0:
			z7 = z7+x8
			x8 = x/z7
			z7 = x8/z7
			paths.append(1)
		else:
			x8 = x8/5
			paths.append(2)
		if x < 3:
			x = x8+3
			z7 = z7-9
			x = 2*x
			paths.append(3)
		else:
			x8 = x8*x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))