import numpy as np 

def function(x):

	a2 = 1
	o9 = 2
	paths = []
	try:
		if o9 < 0:
			x = 0+o9
			a2 = a2+0
			x = x+8
			paths.append(1)
		else:
			x = x-3
			o9 = 0-7
			x = x/6
			paths.append(2)
		if a2 > 2:
			a2 = 0+4
			x = x+2
			paths.append(3)
		else:
			o9 = o9-o9
			o9 = o9/x
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