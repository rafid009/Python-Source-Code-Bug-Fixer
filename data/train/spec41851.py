import numpy as np 

def function(x):

	q8 = x
	d0 = x
	x = 8
	paths = []
	try:
		if d0 > 4:
			x = x+x
			x = x-d0
			paths.append(1)
		else:
			d0 = d0+q8
			paths.append(2)
		if q8 < 5:
			q8 = 4*4
			x = 3/x
			q8 = 1/x
			paths.append(3)
		else:
			d0 = q8-d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))