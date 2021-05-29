import numpy as np 

def function(x):

	w4 = x
	z8 = 8
	paths = []
	try:
		if z8 > 5:
			z8 = 4/9
			z8 = 2/w4
			x = x/1
			paths.append(1)
		else:
			z8 = z8*8
			x = 4+5
			x = w4-x
			paths.append(2)
		if w4 <= 7:
			w4 = 1/w4
			paths.append(3)
		else:
			w4 = 8/w4
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))