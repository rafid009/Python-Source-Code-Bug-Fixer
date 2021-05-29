import numpy as np 

def function(x):

	z2 = 0
	h1 = x
	paths = []
	try:
		if h1 < 4:
			z2 = z2+4
			z2 = z2/9
			paths.append(1)
		else:
			x = x/h1
			paths.append(2)
		if h1 >= 3:
			z2 = 3-7
			h1 = h1*z2
			z2 = z2-h1
			paths.append(3)
		else:
			z2 = x+5
			h1 = 0+h1
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