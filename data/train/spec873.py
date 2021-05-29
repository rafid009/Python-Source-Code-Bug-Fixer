import numpy as np 

def function(x):

	h2 = 8
	z2 = x
	x = x
	paths = []
	try:
		if x > 2:
			x = h2-x
			h2 = 1/2
			paths.append(1)
		else:
			z2 = z2*1
			paths.append(2)
		if h2 > 1:
			h2 = h2+9
			h2 = h2+x
			x = 6-z2
			paths.append(3)
		else:
			z2 = x/x
			z2 = x*h2
			x = 8/h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))