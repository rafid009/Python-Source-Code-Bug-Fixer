import numpy as np 

def function(x):

	b8 = 5
	d0 = x
	x = 4
	paths = []
	try:
		if x >= 4:
			d0 = x*6
			x = x*1
			x = x*1
			paths.append(1)
		else:
			x = b8-9
			paths.append(2)
		if d0 < 8:
			b8 = b8-9
			x = 8+x
			x = x-d0
			paths.append(3)
		else:
			d0 = 9*d0
			d0 = 1-d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))