import numpy as np 

def function(x):

	z2 = 5
	h8 = 9
	paths = []
	try:
		if x <= 7:
			h8 = h8/x
			h8 = h8+h8
			paths.append(1)
		else:
			x = 3/9
			x = 4-x
			paths.append(2)
		if h8 > 9:
			z2 = x/5
			paths.append(3)
		else:
			h8 = 8+h8
			z2 = z2*9
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))