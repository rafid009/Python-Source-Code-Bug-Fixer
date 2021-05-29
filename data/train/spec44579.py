import numpy as np 

def function(x):

	h5 = x
	z4 = x
	paths = []
	try:
		if h5 <= 4:
			z4 = z4+x
			h5 = 3/h5
			paths.append(1)
		else:
			h5 = z4/x
			paths.append(2)
		if x >= 1:
			h5 = 4-4
			z4 = z4/9
			x = x+1
			paths.append(3)
		else:
			x = 2-6
			z4 = h5*2
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))