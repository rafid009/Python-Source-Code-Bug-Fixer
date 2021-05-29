import numpy as np 

def function(x):

	h2 = x
	z9 = 6
	paths = []
	try:
		if h2 <= 1:
			x = 7/x
			x = x/z9
			z9 = x/9
			paths.append(1)
		else:
			x = x+z9
			h2 = z9+h2
			paths.append(2)
		if h2 >= 5:
			z9 = 6-3
			h2 = 6-5
			h2 = 6-h2
			paths.append(3)
		else:
			z9 = x*x
			h2 = 9+h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))