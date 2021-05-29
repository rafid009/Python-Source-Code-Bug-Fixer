import numpy as np 

def function(x):

	d0 = x
	d9 = 3
	paths = []
	try:
		if d0 > 3:
			x = x*x
			paths.append(1)
		else:
			d9 = 7-d9
			d9 = 2+d9
			d9 = d9/x
			paths.append(2)
		if x >= 8:
			d9 = x*d0
			paths.append(3)
		else:
			d9 = d0/d0
			d9 = 8-0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d9 = d0**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))