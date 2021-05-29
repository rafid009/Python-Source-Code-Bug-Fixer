import numpy as np 

def function(x):

	z5 = x
	h7 = 2
	paths = []
	try:
		if h7 < 3:
			h7 = z5/2
			paths.append(1)
		else:
			z5 = z5/2
			z5 = 4*3
			paths.append(2)
		if z5 > 6:
			z5 = z5+6
			x = 9*0
			h7 = 9+h7
			paths.append(3)
		else:
			z5 = z5+x
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