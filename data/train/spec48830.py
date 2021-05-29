import numpy as np 

def function(x):

	d8 = x
	d1 = x
	x = 6
	paths = []
	try:
		if d1 < 4:
			d1 = 7*d1
			paths.append(1)
		else:
			d8 = d8-7
			x = 4-5
			paths.append(2)
		if d8 >= 0:
			x = d1*x
			d1 = 3/5
			d1 = 3-d1
			paths.append(3)
		else:
			d1 = 7/4
			d8 = 3/d8
			d1 = x/d1
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