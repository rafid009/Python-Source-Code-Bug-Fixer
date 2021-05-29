import numpy as np 

def function(x):

	e7 = 3
	d8 = 5
	paths = []
	try:
		if x > 6:
			e7 = e7+d8
			d8 = d8-d8
			paths.append(1)
		else:
			e7 = e7-5
			d8 = 7/d8
			paths.append(2)
		if d8 >= 0:
			x = d8-1
			paths.append(3)
		else:
			d8 = d8-0
			d8 = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))