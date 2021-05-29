import numpy as np 

def function(x):

	z2 = 6
	h0 = 2
	paths = []
	try:
		if z2 > 3:
			h0 = h0*x
			x = x*4
			x = z2*h0
			paths.append(1)
		else:
			x = 2+x
			z2 = z2-z2
			z2 = 2/5
			paths.append(2)
		if z2 <= 9:
			h0 = h0/9
			h0 = 8+h0
			z2 = 6*z2
			paths.append(3)
		else:
			z2 = 1+z2
			x = h0-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))