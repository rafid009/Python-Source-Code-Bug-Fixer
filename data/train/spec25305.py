import numpy as np 

def function(x):

	i0 = 0
	d7 = 7
	paths = []
	try:
		if d7 > 4:
			d7 = d7-8
			d7 = 1/d7
			i0 = 6/x
			paths.append(1)
		else:
			i0 = 5*d7
			paths.append(2)
		if x >= 7:
			x = x-d7
			paths.append(3)
		else:
			x = 6*x
			d7 = 2/4
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		d7 = i0**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))