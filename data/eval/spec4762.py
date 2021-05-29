import numpy as np 

def function(x):

	z9 = 0
	h0 = 1
	x = x
	paths = []
	try:
		if h0 < 1:
			x = x*7
			paths.append(1)
		else:
			h0 = h0+h0
			paths.append(2)
		if z9 < 0:
			z9 = z9+0
			paths.append(3)
		else:
			x = x*h0
			x = 1-3
			h0 = x*2
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