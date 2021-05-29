import numpy as np 

def function(x):

	o4 = x
	x4 = 8
	paths = []
	try:
		if o4 > 9:
			o4 = o4-3
			o4 = 1-0
			paths.append(1)
		else:
			o4 = 4-o4
			paths.append(2)
		if x >= 6:
			o4 = o4*7
			o4 = o4+x
			o4 = o4+1
			paths.append(3)
		else:
			x4 = 7+o4
			x4 = x4*o4
			x = x4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))