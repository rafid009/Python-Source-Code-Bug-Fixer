import numpy as np 

def function(x):

	x0 = x
	o4 = 9
	x = x
	paths = []
	try:
		if x0 < 4:
			x = x*6
			x = 1-9
			o4 = o4-3
			paths.append(1)
		else:
			x = x/1
			o4 = o4-x0
			x0 = o4*9
			paths.append(2)
		if x0 < 2:
			o4 = o4-1
			x0 = x0+x0
			x = x-2
			paths.append(3)
		else:
			x0 = x0*o4
			x0 = x0/x0
			x0 = x0-o4
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