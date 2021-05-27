import numpy as np 

def function(x):

	h3 = 6
	t8 = 2
	paths = []
	try:
		if h3 > 2:
			t8 = 9-x
			h3 = h3-7
			paths.append(1)
		else:
			h3 = 1/h3
			paths.append(2)
		if t8 > 4:
			t8 = t8*h3
			paths.append(3)
		else:
			x = x/4
			h3 = h3*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))