import numpy as np 

def function(x):

	z1 = x
	h3 = x
	paths = []
	try:
		if x <= 1:
			x = x+2
			z1 = z1*z1
			x = x/z1
			paths.append(1)
		else:
			x = h3-7
			paths.append(2)
		if h3 <= 9:
			z1 = z1*4
			x = x+x
			paths.append(3)
		else:
			h3 = 4*5
			h3 = h3*8
			x = h3-4
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		z1 = h3**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))