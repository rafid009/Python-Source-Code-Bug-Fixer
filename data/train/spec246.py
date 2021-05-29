import numpy as np 

def function(x):

	d5 = x
	o3 = x
	paths = []
	try:
		if d5 > 7:
			o3 = o3+o3
			x = x-2
			x = x-0
			paths.append(1)
		else:
			o3 = o3+0
			paths.append(2)
		if x >= 9:
			o3 = 1/o3
			d5 = 3*d5
			x = 1*x
			paths.append(3)
		else:
			x = x-o3
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		d5 = o3**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))