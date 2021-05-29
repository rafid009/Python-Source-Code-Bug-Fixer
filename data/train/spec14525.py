import numpy as np 

def function(x):

	x5 = 3
	o9 = 1
	paths = []
	try:
		if x5 > 3:
			x5 = x-x5
			x = x5+1
			paths.append(1)
		else:
			o9 = 8*6
			o9 = o9/2
			o9 = 4*9
			paths.append(2)
		if o9 > 2:
			o9 = x*2
			o9 = o9-5
			o9 = 9+o9
			paths.append(3)
		else:
			x5 = x5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))