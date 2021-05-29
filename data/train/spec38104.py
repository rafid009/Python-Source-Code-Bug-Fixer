import numpy as np 

def function(x):

	d7 = x
	v8 = 3
	paths = []
	try:
		if d7 < 0:
			x = 8+7
			d7 = d7-1
			paths.append(1)
		else:
			d7 = 0/d7
			v8 = v8+7
			paths.append(2)
		if d7 > 0:
			v8 = 9-v8
			paths.append(3)
		else:
			x = 0-x
			d7 = v8/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))