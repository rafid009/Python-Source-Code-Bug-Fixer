import numpy as np 

def function(x):

	d3 = 0
	o3 = 8
	paths = []
	try:
		if x > 5:
			x = x/x
			paths.append(1)
		else:
			o3 = 4*9
			paths.append(2)
		if x > 1:
			x = 1+o3
			paths.append(3)
		else:
			x = x/8
			o3 = 3/o3
			o3 = 7*x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		d3 = o3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))