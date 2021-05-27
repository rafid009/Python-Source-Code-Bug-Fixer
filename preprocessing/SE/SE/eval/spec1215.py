import numpy as np 

def function(x):

	h0 = x
	d4 = x
	paths = []
	try:
		if d4 <= 6:
			x = x-7
			paths.append(1)
		else:
			d4 = 3*d4
			d4 = 7*3
			x = 5+8
			paths.append(2)
		if d4 >= 9:
			x = 3/h0
			paths.append(3)
		else:
			h0 = x/6
			h0 = h0+d4
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		d4 = h0**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))