import numpy as np 

def function(x):

	d3 = x
	x4 = x
	x = x
	paths = []
	try:
		if x > 4:
			x = x+4
			x = x/x4
			x = x*d3
			paths.append(1)
		else:
			x = 0-x
			x4 = 8*x4
			x4 = x4/9
			paths.append(2)
		if x4 <= 1:
			x = x/x4
			x4 = 4*x4
			paths.append(3)
		else:
			d3 = 4-d3
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		d3 = x4**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))