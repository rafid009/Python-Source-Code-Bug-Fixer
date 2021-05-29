import numpy as np 

def function(x):

	z2 = x
	h7 = 9
	paths = []
	try:
		if x > 9:
			x = x+x
			paths.append(1)
		else:
			x = z2+4
			h7 = h7/z2
			x = x/5
			paths.append(2)
		if z2 > 1:
			h7 = 1*h7
			x = 2/x
			paths.append(3)
		else:
			z2 = z2*z2
			x = 6+h7
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))