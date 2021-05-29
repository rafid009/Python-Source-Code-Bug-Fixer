import numpy as np 

def function(x):

	d9 = x
	h0 = 9
	paths = []
	try:
		if d9 >= 7:
			d9 = 1*d9
			d9 = 4*1
			paths.append(1)
		else:
			h0 = x-8
			d9 = d9*3
			paths.append(2)
		if h0 < 2:
			h0 = 6+4
			d9 = 9*1
			paths.append(3)
		else:
			x = x*0
			x = d9*0
			d9 = h0-d9
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