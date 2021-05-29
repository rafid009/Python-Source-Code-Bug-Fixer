import numpy as np 

def function(x):

	d5 = x
	o3 = x
	paths = []
	try:
		if o3 < 4:
			o3 = 0-6
			x = 5+o3
			paths.append(1)
		else:
			x = d5*o3
			paths.append(2)
		if o3 > 9:
			o3 = o3+4
			o3 = 7/o3
			x = 6-o3
			paths.append(3)
		else:
			o3 = 8-o3
			o3 = x*o3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))