import numpy as np 

def function(x):

	h4 = 3
	o9 = 2
	paths = []
	try:
		if x <= 3:
			o9 = o9-h4
			x = h4+x
			paths.append(1)
		else:
			h4 = h4/7
			x = 7+x
			paths.append(2)
		if o9 <= 3:
			h4 = 6-6
			paths.append(3)
		else:
			o9 = o9-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))