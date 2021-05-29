import numpy as np 

def function(x):

	z1 = x
	h1 = x
	paths = []
	try:
		if z1 < 1:
			z1 = 3/z1
			x = x/9
			z1 = z1-2
			paths.append(1)
		else:
			h1 = h1+h1
			h1 = h1*1
			paths.append(2)
		if h1 > 7:
			x = 3-4
			paths.append(3)
		else:
			z1 = z1+h1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		h1 = z1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))