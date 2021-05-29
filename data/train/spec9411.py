import numpy as np 

def function(x):

	o0 = x
	a7 = 8
	paths = []
	try:
		if o0 <= 6:
			o0 = a7+4
			o0 = o0-x
			paths.append(1)
		else:
			a7 = a7/8
			paths.append(2)
		if x >= 9:
			x = o0/x
			paths.append(3)
		else:
			a7 = 0+o0
			a7 = a7/7
			a7 = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))