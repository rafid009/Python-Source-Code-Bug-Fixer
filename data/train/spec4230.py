import numpy as np 

def function(x):

	o4 = x
	d0 = 1
	paths = []
	try:
		if o4 <= 2:
			x = x*7
			x = 6/1
			x = x+9
			paths.append(1)
		else:
			x = o4*x
			paths.append(2)
		if d0 < 9:
			d0 = d0+5
			paths.append(3)
		else:
			x = x-0
			d0 = d0-2
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))