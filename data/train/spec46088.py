import numpy as np 

def function(x):

	z9 = x
	h8 = 1
	paths = []
	try:
		if z9 <= 1:
			h8 = h8/z9
			paths.append(1)
		else:
			x = h8*h8
			h8 = h8/h8
			h8 = 7/7
			paths.append(2)
		if z9 <= 5:
			h8 = 1/3
			z9 = h8-z9
			paths.append(3)
		else:
			z9 = 0+z9
			x = x*5
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		h8 = z9**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))