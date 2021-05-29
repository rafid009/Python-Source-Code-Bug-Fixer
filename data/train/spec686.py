import numpy as np 

def function(x):

	h7 = 6
	z4 = x
	paths = []
	try:
		if x > 9:
			x = z4*1
			x = x/5
			x = 3*4
			paths.append(1)
		else:
			h7 = h7+z4
			z4 = z4+0
			paths.append(2)
		if z4 < 4:
			h7 = 1*x
			x = 7/4
			h7 = h7-h7
			paths.append(3)
		else:
			z4 = z4+9
			x = x+z4
			x = z4*x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		h7 = z4**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))