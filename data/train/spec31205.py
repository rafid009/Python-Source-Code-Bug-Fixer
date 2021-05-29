import numpy as np 

def function(x):

	o9 = 7
	e7 = 8
	paths = []
	try:
		if x > 1:
			o9 = 5/2
			paths.append(1)
		else:
			o9 = e7+o9
			o9 = o9*e7
			paths.append(2)
		if o9 < 6:
			e7 = 6+6
			o9 = o9-o9
			o9 = o9+o9
			paths.append(3)
		else:
			e7 = e7/9
			x = 8+7
			x = 0-8
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