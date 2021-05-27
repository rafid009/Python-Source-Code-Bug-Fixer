import numpy as np 

def function(x):

	o4 = x
	h3 = 4
	paths = []
	try:
		if x < 5:
			h3 = x/h3
			paths.append(1)
		else:
			h3 = 2/1
			h3 = h3-4
			paths.append(2)
		if x > 9:
			x = o4+o4
			paths.append(3)
		else:
			o4 = o4-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))