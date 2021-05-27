import numpy as np 

def function(x):

	o3 = x
	d9 = x
	paths = []
	try:
		if o3 <= 5:
			d9 = d9*o3
			paths.append(1)
		else:
			x = 5+3
			d9 = x-d9
			x = 4-x
			paths.append(2)
		if d9 < 6:
			x = 3*o3
			o3 = 3+o3
			paths.append(3)
		else:
			o3 = 7+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))