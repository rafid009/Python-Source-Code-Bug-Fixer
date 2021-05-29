import numpy as np 

def function(x):

	o4 = x
	d8 = 5
	paths = []
	try:
		if x <= 0:
			x = x/o4
			paths.append(1)
		else:
			o4 = o4+2
			o4 = 9-o4
			paths.append(2)
		if x < 9:
			o4 = o4+d8
			paths.append(3)
		else:
			x = x-3
			o4 = o4*x
			d8 = d8/6
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		d8 = o4**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))