import numpy as np 

def function(x):

	z8 = 3
	r7 = x
	paths = []
	try:
		if x >= 2:
			z8 = z8+1
			r7 = 9-r7
			r7 = 7*7
			paths.append(1)
		else:
			z8 = z8*6
			z8 = z8+x
			paths.append(2)
		if z8 < 8:
			x = z8*4
			paths.append(3)
		else:
			x = 3-z8
			x = 8-1
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		r7 = z8**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))