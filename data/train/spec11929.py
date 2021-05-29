import numpy as np 

def function(x):

	z4 = 6
	h7 = x
	x = 7
	paths = []
	try:
		if h7 < 7:
			z4 = 5-z4
			z4 = z4/9
			paths.append(1)
		else:
			h7 = x*8
			paths.append(2)
		if z4 >= 9:
			x = x/8
			paths.append(3)
		else:
			x = z4*z4
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))