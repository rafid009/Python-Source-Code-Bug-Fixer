import numpy as np 

def function(x):

	h0 = 8
	z4 = x
	x = x
	paths = []
	try:
		if h0 >= 5:
			h0 = 1-8
			paths.append(1)
		else:
			z4 = 9+0
			z4 = 9/z4
			paths.append(2)
		if z4 > 3:
			x = 5+x
			paths.append(3)
		else:
			h0 = 4/4
			x = x+9
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))