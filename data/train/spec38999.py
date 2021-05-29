import numpy as np 

def function(x):

	d0 = x
	q3 = x
	paths = []
	try:
		if d0 > 8:
			x = q3*x
			paths.append(1)
		else:
			q3 = q3+q3
			paths.append(2)
		if q3 >= 6:
			d0 = 9/d0
			x = x-d0
			paths.append(3)
		else:
			x = 6/x
			x = x-q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))