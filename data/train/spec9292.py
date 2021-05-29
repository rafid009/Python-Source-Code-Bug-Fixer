import numpy as np 

def function(x):

	d7 = 6
	h8 = x
	paths = []
	try:
		if h8 <= 8:
			x = h8/d7
			paths.append(1)
		else:
			d7 = h8+d7
			h8 = h8*3
			paths.append(2)
		if d7 >= 4:
			d7 = d7-1
			paths.append(3)
		else:
			d7 = 2/d7
			x = 3*d7
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		d7 = h8**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))