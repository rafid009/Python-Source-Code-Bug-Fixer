import numpy as np 

def function(x):

	d3 = x
	u2 = x
	paths = []
	try:
		if d3 >= 6:
			u2 = u2/2
			paths.append(1)
		else:
			d3 = x/3
			paths.append(2)
		if u2 <= 1:
			x = x-5
			x = 2-9
			x = 8-x
			paths.append(3)
		else:
			d3 = d3-3
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		d3 = u2**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))