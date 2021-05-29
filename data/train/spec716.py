import numpy as np 

def function(x):

	d4 = 3
	h4 = 0
	paths = []
	try:
		if d4 <= 7:
			d4 = 9-6
			paths.append(1)
		else:
			x = 9/x
			x = 0-4
			d4 = d4-h4
			paths.append(2)
		if h4 > 4:
			d4 = d4-6
			d4 = 4/d4
			paths.append(3)
		else:
			d4 = 8*2
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