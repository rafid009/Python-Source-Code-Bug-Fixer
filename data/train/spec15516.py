import numpy as np 

def function(x):

	h5 = x
	d0 = 7
	paths = []
	try:
		if d0 >= 7:
			d0 = d0+2
			x = d0-x
			paths.append(1)
		else:
			d0 = 1+d0
			paths.append(2)
		if h5 < 1:
			d0 = d0-0
			x = 1+x
			paths.append(3)
		else:
			x = x*7
			x = 0-x
			x = d0+8
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		d0 = h5**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))