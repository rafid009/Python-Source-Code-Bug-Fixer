import numpy as np 

def function(x):

	d8 = x
	d0 = 0
	paths = []
	try:
		if x > 9:
			x = 6-x
			d8 = x+d0
			x = x-4
			paths.append(1)
		else:
			d0 = d0/1
			d8 = 4/2
			paths.append(2)
		if x >= 1:
			d8 = 3/d8
			paths.append(3)
		else:
			d0 = d0*d0
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))