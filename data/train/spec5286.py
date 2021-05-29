import numpy as np 

def function(x):

	z9 = 5
	h7 = x
	paths = []
	try:
		if x <= 3:
			x = x*z9
			paths.append(1)
		else:
			z9 = 7-x
			paths.append(2)
		if h7 > 7:
			h7 = h7/8
			x = 8-x
			paths.append(3)
		else:
			z9 = 7+z9
			x = h7/z9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		h7 = z9**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))