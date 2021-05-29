import numpy as np 

def function(x):

	z2 = x
	h7 = 2
	paths = []
	try:
		if h7 > 8:
			h7 = h7+9
			paths.append(1)
		else:
			x = h7/x
			z2 = 2/z2
			x = x/x
			paths.append(2)
		if x <= 9:
			x = 8-3
			paths.append(3)
		else:
			x = 1+x
			z2 = z2+z2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		h7 = z2**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))