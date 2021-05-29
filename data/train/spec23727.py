import numpy as np 

def function(x):

	h9 = x
	d1 = x
	x = 2
	paths = []
	try:
		if d1 > 9:
			h9 = h9/h9
			h9 = h9+3
			h9 = h9+1
			paths.append(1)
		else:
			d1 = 4/1
			x = d1+2
			paths.append(2)
		if x > 8:
			h9 = h9-d1
			h9 = h9/x
			paths.append(3)
		else:
			d1 = d1/d1
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		x = h9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))