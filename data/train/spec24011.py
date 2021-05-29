import numpy as np 

def function(x):

	o2 = x
	x4 = 5
	paths = []
	try:
		if o2 < 2:
			x = o2/x
			o2 = o2/7
			x = x-9
			paths.append(1)
		else:
			o2 = 3+o2
			x4 = x4-2
			paths.append(2)
		if x > 7:
			x = 8*7
			x4 = 3-x4
			x4 = x4+2
			paths.append(3)
		else:
			o2 = o2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))