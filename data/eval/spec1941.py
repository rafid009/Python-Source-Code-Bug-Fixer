import numpy as np 

def function(x):

	x8 = 4
	d8 = x
	paths = []
	try:
		if x > 3:
			x8 = x-x8
			x8 = 9/x8
			paths.append(1)
		else:
			x = 9+6
			x = d8-3
			x8 = x8-8
			paths.append(2)
		if x8 > 6:
			d8 = d8+8
			d8 = 0/d8
			x = x*d8
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		d8 = x8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))