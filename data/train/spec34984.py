import numpy as np 

def function(x):

	h0 = x
	z9 = x
	paths = []
	try:
		if h0 <= 9:
			z9 = z9/1
			x = 8-h0
			x = x+2
			paths.append(1)
		else:
			z9 = z9-h0
			z9 = 8/9
			paths.append(2)
		if x > 9:
			z9 = 0/5
			x = h0*x
			z9 = h0+0
			paths.append(3)
		else:
			z9 = 0*h0
			z9 = z9+z9
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))