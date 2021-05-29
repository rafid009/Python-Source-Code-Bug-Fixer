import numpy as np 

def function(x):

	t8 = x
	h3 = x
	paths = []
	try:
		if t8 < 2:
			h3 = h3-6
			t8 = 4/x
			paths.append(1)
		else:
			h3 = 3+h3
			h3 = x+h3
			paths.append(2)
		if x > 2:
			h3 = h3*5
			paths.append(3)
		else:
			x = t8+x
			h3 = h3/6
			t8 = h3-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))