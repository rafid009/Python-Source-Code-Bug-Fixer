import numpy as np 

def function(x):

	h2 = 2
	z6 = x
	paths = []
	try:
		if h2 >= 4:
			z6 = 8+x
			paths.append(1)
		else:
			x = z6/h2
			x = 0+3
			paths.append(2)
		if z6 > 4:
			z6 = z6-9
			h2 = x/7
			x = z6-x
			paths.append(3)
		else:
			x = z6*9
			h2 = h2-6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))