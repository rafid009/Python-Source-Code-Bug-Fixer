import numpy as np 

def function(x):

	d8 = 1
	o7 = x
	paths = []
	try:
		if d8 < 6:
			o7 = o7*9
			o7 = o7-x
			paths.append(1)
		else:
			o7 = o7/1
			d8 = o7/1
			d8 = d8*d8
			paths.append(2)
		if d8 >= 6:
			d8 = 7/o7
			o7 = 3/o7
			paths.append(3)
		else:
			x = 8-x
			d8 = x*x
			o7 = d8-6
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))