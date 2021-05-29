import numpy as np 

def function(x):

	h6 = 2
	z5 = 9
	paths = []
	try:
		if z5 < 0:
			z5 = 0+z5
			x = 6+x
			x = x/4
			paths.append(1)
		else:
			z5 = 3-8
			x = x*6
			paths.append(2)
		if x <= 6:
			x = 3+x
			x = 3*1
			h6 = 4+9
			paths.append(3)
		else:
			h6 = 6/h6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		h6 = z5**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))