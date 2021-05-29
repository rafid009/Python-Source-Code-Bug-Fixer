import numpy as np 

def function(x):

	o4 = 0
	d9 = 4
	paths = []
	try:
		if x > 5:
			o4 = 0-o4
			x = 5+3
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if o4 > 1:
			o4 = d9/o4
			d9 = o4/3
			paths.append(3)
		else:
			o4 = o4+x
			d9 = 6+o4
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