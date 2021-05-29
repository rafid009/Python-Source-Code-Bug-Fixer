import numpy as np 

def function(x):

	d9 = 4
	h3 = 9
	paths = []
	try:
		if x < 7:
			h3 = h3-h3
			h3 = h3-9
			x = 0*x
			paths.append(1)
		else:
			h3 = h3/9
			paths.append(2)
		if x >= 3:
			d9 = x/h3
			paths.append(3)
		else:
			d9 = 6-d9
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))